#!/usr/bin/env python3
from pathlib import Path
import csv,json,re,subprocess,sys,hashlib
import yaml
from jsonschema import validate as schema_validate
VALIDATOR_VERSION="5.1.0"

def norm_hash(p):
    b=p.read_bytes().replace(b"\r\n",b"\n").replace(b"\r",b"\n"); return hashlib.sha256(b).hexdigest()

def validate(root):
    root=Path(root); results=[]
    def ok(name,cond,detail=""):
        results.append({'check':name,'status':'PASS' if cond else 'FAIL','detail':str(detail)})
    spec=yaml.safe_load((root/'spec/SKILL_SPEC.yaml').read_text(encoding='utf-8')); schema=json.loads((root/'spec/SKILL_SPEC_SCHEMA.json').read_text(encoding='utf-8')); schema_validate(spec,schema)
    skill=root/spec['release']['skill_root']
    ok('validator_version',spec['toolchain']['validator_version']==VALIDATOR_VERSION,spec['toolchain']['validator_version'])
    # module files and unique ids
    mids=[m['id'] for m in spec['modules']]; ok('module_ids_unique',len(mids)==len(set(mids)),mids)
    missing=[m['path'] for m in spec['modules'] if not (skill/m['path']).is_file()]; ok('module_paths_exist',not missing,missing)
    # builder drift
    p=subprocess.run([sys.executable,str(root/'tooling/build_runtime.py'),str(root),'--check'],capture_output=True,text=True)
    ok('generated_runtime_no_drift',p.returncode==0,(p.stdout+p.stderr).strip())
    # runtime locator
    loc=list(csv.DictReader((skill/spec['generated_outputs']['rule_locator_index']).open(encoding='utf-8')))
    rule_ids=[r['rule_id'] for r in loc]
    ok('rule_ids_unique',len(rule_ids)==len(set(rule_ids)),[x for x in set(rule_ids) if rule_ids.count(x)>1])
    ok('rule_count_211',len(rule_ids)==211,len(rule_ids))
    for rid in ['EMP-DATA09A','EMP-DATA09B','CORE-L4-10']:
        ok('rule_present:'+rid,rid in set(rule_ids),rid)
    # command boundary
    cmds=list(csv.DictReader((skill/spec['generated_outputs']['commands']).open(encoding='utf-8'))); toks={r['token'].upper() for r in cmds}
    ok('commands_exact_RE_AU',toks=={'RE','AU'},sorted(toks))
    # optional profile not default-routed
    tasks=list(csv.DictReader((skill/spec['generated_outputs']['task_router']).open(encoding='utf-8')))
    contamination=[r['task_class'] for r in tasks if r['task_class']!='AI_FINANCE_RESEARCH' and re.search(r'(^|\+)\s*03\b',r['required_modules'])]
    ok('ai_profile_not_default_routed',not contamination,contamination)
    # gate ids referenced by semantic prose
    gates={g['gate_id'] for g in spec['gates']}; unresolved=[]
    for m in spec['modules']:
        pth=skill/m['path'];
        for tok in re.findall(r'\bGATE-[A-Z0-9\-]+\b',pth.read_text(encoding='utf-8')):
            if tok not in gates: unresolved.append((m['id'],tok))
    ok('gate_refs_resolve',not unresolved,unresolved[:20])
    # method source ids must resolve to rules, allowing source records keyed to implementation source rule
    src=list(csv.DictReader((skill/spec['generated_outputs']['method_source_locator_registry']).open(encoding='utf-8')))
    badsrc=sorted({r['rule_id'] for r in src if r['rule_id'] not in set(rule_ids)})
    ok('method_source_rule_ids_resolve',not badsrc,badsrc)
    # source-pointer and source-value corrections
    sources=(skill/spec['generated_outputs']['method_source_locator_registry']).read_text(encoding='utf-8')
    alltxt='\n'.join((skill/m['path']).read_text(encoding='utf-8') for m in spec['modules'])
    ok('blindness_source_pointer_resolved','EMP-BLIND01' in sources and 'methodological source for the blindness principle is registered under `EMP-BLIND01`' in alltxt,'')
    ok('missing_data_doi_correct','10.1093/rfs/hhae036' in sources and '10.1093/rfs/hhae056' not in sources,'')
    ok('hlz_threshold_correct','3.54' in alltxt and '3.47' not in alltxt,'')
    # evidence-sufficiency and screen/formal boundaries
    core=(skill/'modules/01_CORE_RESEARCH_WORKFLOW_EN.md').read_text(encoding='utf-8')
    emp=(skill/'modules/02_EMPIRICAL_DATA_PILOT_METHODS_EN.md').read_text(encoding='utf-8')
    ok('literature_weak_evidence_not_narrow','verification lead' in core and 'cannot trigger formal `L4_NARROW`' in core,'')
    ok('screen_resource_only','resource-allocation' in emp and 'not a formal `ECONOMIC_MINIMUM`' in emp,'')
    # professional public terminology / no legacy runtime tokens
    semantic='\n'.join((skill/m['path']).read_text(encoding='utf-8') for m in spec['modules'])
    runtime='\n'.join((skill/p).read_text(encoding='utf-8') for p in spec['generated_outputs'].values())
    forbidden=['KILL_SOURCE_TIER','PRE_FORMAL_REKILL','L4_KILL_COLLISION','L4_KILL_SO_WHAT','L4_KILL_CONSTRUCT','KILL_COLLISION','KILL_SO_WHAT','KILL_CONSTRUCT','CENSUS_KILL','L4_KILL','DEATH_PILOT','PILOT_VERDICT','POST_PILOT_L4','FILE_LIBRARY_REF']
    hits=[x for x in forbidden if x in semantic or x in runtime]
    ok('no_legacy_runtime_terms',not hits,hits)
    # generic public-release leakage checks; maintainer-specific sensitive strings are checked by detached release tooling.
    generic_leaks=[]
    generic_patterns=[
        (r'[A-Za-z]:\\[^\n`]+', 'absolute_windows_path'),
        (r'Private migration artifact|Canonical-English staging draft|Not yet a public release', 'migration_banner'),
        (r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', 'embedded_email_address'),
    ]
    for pat,label in generic_patterns:
        if re.search(pat,semantic,re.I): generic_leaks.append(label)
    ok('no_generic_public_leakage',not generic_leaks,generic_leaks)
    # installable self-contained refs in SKILL and canonical loader
    refs=[]
    for pth in [skill/'SKILL.md',skill/'00_CANONICAL_INDEX_EN.md']:
        for ref in re.findall(r'`([^`]+\.(?:md|csv))`',pth.read_text(encoding='utf-8')):
            if '/' in ref and not (skill/ref).exists(): refs.append((pth.name,ref))
    ok('loader_refs_self_contained',not refs,refs)
    # source fingerprint scope exists
    missing_scope=[x for x in spec['fingerprint']['scope'] if not (root/x).is_file()]
    ok('source_fingerprint_scope_exists',not missing_scope,missing_scope)
    # state transitions terminology
    sm=(skill/spec['generated_outputs']['state_machine']).read_text(encoding='utf-8')
    ok('preformal_recheck_state','PRE_FORMAL_L4_RECHECK' in sm and 'PRE_FORMAL_L4_REKILL' not in sm,'')
    ok('screen_not_economic_null','the screen never establishes an economic null' in sm.lower(),'')
    return results

def main():
    root=Path(sys.argv[1]); res=validate(root); print(json.dumps({'status':'PASS' if all(x['status']=='PASS' for x in res) else 'FAIL','checks':res},indent=2,ensure_ascii=False)); sys.exit(0 if all(x['status']=='PASS' for x in res) else 1)
if __name__=='__main__': main()
