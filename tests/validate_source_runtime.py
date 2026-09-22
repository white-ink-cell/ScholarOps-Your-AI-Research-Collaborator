#!/usr/bin/env python3
from pathlib import Path
import csv,json,re,subprocess,sys,yaml
ROOT=Path(sys.argv[1])
proc=subprocess.run([sys.executable,str(ROOT/'tooling/validate_runtime.py'),str(ROOT)],capture_output=True,text=True)
try: base=json.loads(proc.stdout)
except Exception:
    print(proc.stdout); print(proc.stderr,file=sys.stderr); raise
checks=list(base['checks'])
def add(name,cond,detail=''): checks.append({'check':name,'status':'PASS' if cond else 'FAIL','detail':str(detail)})
spec=yaml.safe_load((ROOT/'spec/SKILL_SPEC.yaml').read_text(encoding='utf-8'))
skill=ROOT/spec['release']['skill_root']
# Ensure all task module IDs resolve. Conditional module annotations are extracted from digit tokens.
mods={m['id'] for m in spec['modules']}
for row in csv.DictReader((skill/'runtime/TASK_ROUTER.csv').open(encoding='utf-8')):
    ids=set(re.findall(r'(?<![A-Z0-9])(?:00|01|02|03|04|05|06|07|08)(?![A-Z0-9])',row['required_modules']))
    add('task_modules_resolve:'+row['task_class'],ids<=mods,sorted(ids-mods))
# State references resolve to defined or reserved IDs.
states={x['state_id'] for x in spec['states']}; reserved={x['state_id'] for x in spec['reserved_state_ids']}
unknown=[]
for x in spec['states']:
    for field in ['allowed_next','return_or_failure']:
        for sid in re.findall(r'\bS\d+\b',x[field]):
            if sid not in states and sid not in reserved: unknown.append((x['state_id'],field,sid))
add('state_references_resolve',not unknown,unknown)
# Rule locator row count and unique IDs are already checked by validator; ensure every module with rule headings is represented.
loc=list(csv.DictReader((skill/'runtime/RULE_LOCATOR_INDEX.csv').open(encoding='utf-8')))
by_mod={}
for r in loc: by_mod.setdefault(r['module_id'],0); by_mod[r['module_id']]+=1
expected={m['id'] for m in spec['modules'] if m['role']!='canonical_loader'}
add('rule_modules_represented',expected<=set(by_mod),sorted(expected-set(by_mod)))
# English-only machine/runtime layer: prohibit CJK in runtime/spec/tooling/tests.
cjk=re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff]')
hits=[]
for basep in [ROOT/'spec',ROOT/'tooling',ROOT/'tests',skill/'runtime']:
    for p in basep.rglob('*'):
        if p.is_file() and p.suffix.lower() in {'.yaml','.json','.py','.csv','.md','.txt'}:
            if cjk.search(p.read_text(encoding='utf-8',errors='ignore')): hits.append(str(p.relative_to(ROOT)))
add('machine_layer_english_only',not hits,hits)
status='PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL'
print(json.dumps({'status':status,'checks':checks},indent=2,ensure_ascii=False)); sys.exit(0 if status=='PASS' else 1)
