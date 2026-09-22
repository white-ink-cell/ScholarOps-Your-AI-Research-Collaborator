#!/usr/bin/env python3
from pathlib import Path
import argparse, csv, json, re, io
import yaml
from jsonschema import validate as schema_validate

BUILDER_VERSION = "3.0.0"

def load_spec(root):
    spec=yaml.safe_load((root/"spec/SKILL_SPEC.yaml").read_text(encoding="utf-8"))
    schema=json.loads((root/"spec/SKILL_SPEC_SCHEMA.json").read_text(encoding="utf-8"))
    schema_validate(spec,schema)
    return spec

def csv_text(rows, cols):
    out=io.StringIO(); w=csv.DictWriter(out,fieldnames=cols,lineterminator="\n"); w.writeheader()
    for r in rows: w.writerow({c:r.get(c,"") for c in cols})
    return out.getvalue()

def render_outputs(root):
    spec=load_spec(root); skill_root=root/spec["release"]["skill_root"]; out=spec["generated_outputs"]; outputs={}
    outputs[out["controlled_vocabulary"]]=csv_text([{"field":x["field"],"allowed_values":";".join(x["allowed_values"]),"type":x["type"]} for x in spec["fields"]],["field","allowed_values","type"])
    outputs[out["state_machine"]]=csv_text(spec["states"],["state_id","state","owner","entry","required_artifact","pass_condition","allowed_next","return_or_failure","global_precondition"])
    outputs[out["task_router"]]=csv_text(spec["tasks"],["task_class","trigger_examples","required_modules","routing_note"])
    outputs[out["gate_policy"]]=csv_text(spec["gates"],["gate_id","gate","activation_class","trigger","execution"])
    outputs[out["module_registry"]]=csv_text(spec["modules"],["id","path","role","description","load_policy"])
    outputs[out["commands"]]=csv_text(spec["commands"],["token","case_insensitive","mode_field","mode_value","action","precedence","alone_stop","description"])
    outputs[out["semantic_invariants"]]=csv_text(spec["invariants"],["invariant_id","invariant","required_semantics"])
    loc=[]
    for m in spec["modules"]:
        if m["role"]=="canonical_loader": continue
        p=skill_root/m["path"]
        section=""
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "): section=line[2:].strip()
            elif line.startswith("## "):
                mm=re.match(r"## ([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\s+—\s*(.*)$",line)
                if mm: loc.append({"rule_id":mm.group(1),"module_id":m["id"],"section":section,"title":mm.group(2).strip()})
    outputs[out["rule_locator_index"]]=csv_text(loc,["rule_id","module_id","section","title"])
    outputs[out["method_source_locator_registry"]]=csv_text(spec["method_sources"],["rule_id","source","source_type","edition_year","chapter_section","page_or_article_locator","doi_or_stable_id","fulltext_verified","transfer_scope","transfer_status","claim_supported","claim_not_supported"])
    commands=sorted(spec["commands"],key=lambda x:x["precedence"])
    ref=[f'# ScholarOps Runtime Reference — {spec["release"]["version"]}','', '> Generated from the repository source spec. Do not edit by hand.','', '## Workflow shorthands']
    for c in commands:
        ref.append(f'- `{c["token"]}` → {c["action"]}: {c["description"]}')
    ref += ['', '## Precedence', '', ' → '.join(f'`{x}`' for x in spec['precedence_chain']), '', '## Empirical execution classes','']
    fm={x['field']:x['allowed_values'] for x in spec['fields']}
    for v in fm.get('EMPIRICAL_EXECUTION_CLASS',[]): ref.append(f'- `{v}`')
    ref += ['', '## Runtime registries','', '- `runtime/CANONICAL_STATE_MACHINE.csv`', '- `runtime/CONTROLLED_VOCABULARY_REGISTRY.csv`', '- `runtime/TASK_ROUTER.csv`', '- `runtime/GATE_ACTIVATION_POLICY.csv`', '- `runtime/RULE_LOCATOR_INDEX.csv`', '- `references/METHOD_SOURCE_REGISTRY.csv`','']
    outputs[out['runtime_reference']]="\n".join(ref)
    return skill_root, outputs

def write_outputs(root):
    skill_root,outputs=render_outputs(root)
    for rel,text in outputs.items():
        p=skill_root/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text,encoding='utf-8',newline='\n')
    return outputs

def check_outputs(root):
    skill_root,outputs=render_outputs(root); bad=[]
    for rel,text in outputs.items():
        p=skill_root/rel
        if not p.is_file() or p.read_bytes()!=text.encode('utf-8'): bad.append(rel)
    return bad

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root'); ap.add_argument('--check',action='store_true'); args=ap.parse_args(); root=Path(args.root)
    spec=load_spec(root)
    if spec['toolchain']['builder_version']!=BUILDER_VERSION: raise SystemExit('builder version mismatch')
    if args.check:
        bad=check_outputs(root); print(json.dumps({'status':'PASS' if not bad else 'FAIL','generated_drift':bad},ensure_ascii=False)); raise SystemExit(0 if not bad else 1)
    outs=write_outputs(root); print(json.dumps({'status':'PASS','generated':list(outs)},ensure_ascii=False))
if __name__=='__main__': main()
