#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
SKILL = ROOT / 'skills' / 'scholarops'

checks = []
def add(name, ok, detail=''):
    checks.append((name, bool(ok), str(detail)))

required = [
    ROOT/'README.md', ROOT/'README_CN.md', ROOT/'LICENSE', ROOT/'CITATION.cff',
    ROOT/'quickstart/QUICK_START.md', ROOT/'quickstart/QUICK_START_CN.md',
    SKILL/'SKILL.md', SKILL/'00_CANONICAL_INDEX_EN.md', SKILL/'00_CANONICAL_INDEX_CN.md',
]
for p in required:
    add(f'required:{p.relative_to(ROOT)}', p.is_file())

pairs = [
    (SKILL/'00_CANONICAL_INDEX_EN.md', SKILL/'00_CANONICAL_INDEX_CN.md'),
    (SKILL/'modules/01_CORE_RESEARCH_WORKFLOW_EN.md', SKILL/'modules/01_CORE_RESEARCH_WORKFLOW_CN.md'),
    (SKILL/'modules/02_EMPIRICAL_DATA_PILOT_METHODS_EN.md', SKILL/'modules/02_EMPIRICAL_DATA_PILOT_METHODS_CN.md'),
    (SKILL/'modules/04_ACCESS_INTERFACE_EN.md', SKILL/'modules/04_ACCESS_INTERFACE_CN.md'),
    (SKILL/'modules/05_PROJECT_STATE_EN.md', SKILL/'modules/05_PROJECT_STATE_CN.md'),
    (SKILL/'modules/06_SPECIALIZED_DESIGN_EVALUATION_GATES_EN.md', SKILL/'modules/06_SPECIALIZED_DESIGN_EVALUATION_GATES_CN.md'),
    (SKILL/'modules/07_ARTIFACT_STATE_REPRODUCIBILITY_GOVERNANCE_EN.md', SKILL/'modules/07_ARTIFACT_STATE_REPRODUCIBILITY_GOVERNANCE_CN.md'),
    (SKILL/'governance/HOST_MEMORY_LANGUAGE_EN.md', SKILL/'governance/HOST_MEMORY_LANGUAGE_CN.md'),
    (SKILL/'profiles/ai-finance/PROFILE_EN.md', SKILL/'profiles/ai-finance/PROFILE_CN.md'),
]
heading_rule = re.compile(r'^##+\s+((?:CORE|EMP|GOV|AI|GATE|INV)-[A-Z0-9-]+)\b', re.M)
code_block = re.compile(r'```(?:text)?\n(.*?)```', re.S)
controlled = re.compile(r'\b[A-Z][A-Z0-9_]{2,}\b')
ignore = {
    'DOI','PDF','CSV','JSON','YAML','URL','URLs','README','SKILL','CN','EN','AI','ML','LLM','LLMs','NLP',
    'SEC','CRSP','WRDS','FWER','FDR','SESOI','MDE','OLS','IV','FE','QA','OOS','IID','ID','IDs','API','APIs',
    'CLI','RNG','AIC','CAPM','HTTP','HTTPS'
}
for enp, cnp in pairs:
    en = enp.read_text(encoding='utf-8')
    cn = cnp.read_text(encoding='utf-8')
    er = set(heading_rule.findall(en)); cr = set(heading_rule.findall(cn))
    add(f'bilingual_rule_ids:{enp.relative_to(ROOT)}', er == cr, f'missing={sorted(er-cr)} extra={sorted(cr-er)}')
    def code_tokens(text):
        body='\n'.join(code_block.findall(text))
        return {x for x in controlled.findall(body) if x not in ignore}
    et, ct = code_tokens(en), code_tokens(cn)
    add(f'bilingual_controlled_tokens:{enp.relative_to(ROOT)}', et <= ct, f'missing={sorted(et-ct)}')

# Quick Start is deliberately simple and must not expose Full-Skill command shorthands.
for rel in ['quickstart/QUICK_START.md','quickstart/QUICK_START_CN.md']:
    text=(ROOT/rel).read_text(encoding='utf-8')
    bad=[]
    for cmd in ['RE','AU','EX']:
        if re.search(rf'(?<![A-Za-z0-9_])`?{cmd}`?(?![A-Za-z0-9_])', text): bad.append(cmd)
    add(f'quickstart_no_full_commands:{rel}', not bad, bad)

# No ChatGPT-internal/source-rendering references or local sandbox links may ship publicly.
forbidden_patterns = [
    ('internal_source_marker', re.compile('file' + 'cite|file' + 'cite', re.I)),
    ('local_runtime_link', re.compile('sandbox' + ':/', re.I)),
    ('absolute_windows_path', re.compile(r'(?<![A-Za-z])[A-Za-z]:\\\\')),
]
for name, pat in forbidden_patterns:
    hits=[]
    for p in ROOT.rglob('*'):
        if p.is_file() and '.git' not in p.parts:
            try: txt=p.read_text(encoding='utf-8')
            except Exception: continue
            if pat.search(txt): hits.append(str(p.relative_to(ROOT)))
    add(f'public_no_{name}', not hits, hits)

# Example fixtures are runnable expectations, not decorative prose.
example_root=ROOT/'examples'
for d in sorted(x for x in example_root.iterdir() if x.is_dir()):
    expected={'INPUT.md','EXPECTED_ROUTE.md','EXPECTED_GATES.md','EXPECTED_DECISION.md','README.md'}
    actual={p.name for p in d.iterdir() if p.is_file()}
    add(f'example_fixture:{d.name}', expected <= actual, sorted(expected-actual))

# No PR template in v1.0; Issues only.
pr_candidates=[ROOT/'.github/PULL_REQUEST_TEMPLATE.md', ROOT/'.github/pull_request_template.md', ROOT/'.github/PULL_REQUEST_TEMPLATE']
add('no_pr_template', not any(p.exists() for p in pr_candidates))
issue_dir=ROOT/'.github/ISSUE_TEMPLATE'
add('issue_templates_present', issue_dir.is_dir() and len(list(issue_dir.glob('*.yml'))) >= 3)

# YAML parse checks for citation and issue forms.
try:
    cff=yaml.safe_load((ROOT/'CITATION.cff').read_text(encoding='utf-8'))
    add('citation_yaml_parses', isinstance(cff,dict))
    add('citation_identity', cff.get('title','').startswith('ScholarOps') and cff.get('version')=='1.0.0' and cff.get('license')=='Apache-2.0')
    authors=cff.get('authors') or []
    add('citation_author', len(authors)==1 and authors[0].get('name')=='white-ink-cell')
except Exception as e:
    add('citation_yaml_parses',False,repr(e))

for p in sorted(issue_dir.glob('*.yml')):
    try:
        obj=yaml.safe_load(p.read_text(encoding='utf-8'))
        add(f'issue_yaml:{p.name}', isinstance(obj,dict) and 'name' in obj and 'body' in obj)
    except Exception as e:
        add(f'issue_yaml:{p.name}',False,repr(e))

# Local markdown links in root READMEs and quickstarts must resolve. Ignore URLs/anchors.
link_re=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
for rel in ['README.md','README_CN.md','quickstart/QUICK_START.md','quickstart/QUICK_START_CN.md']:
    p=ROOT/rel; txt=p.read_text(encoding='utf-8')
    missing=[]
    for target in link_re.findall(txt):
        target=target.strip()
        if target.startswith(('http://','https://','#','mailto:')): continue
        target=target.split('#',1)[0]
        if not target: continue
        if not (p.parent/target).resolve().exists(): missing.append(target)
    add(f'local_links:{rel}',not missing,missing)

# README language switch should exist both ways.
add('readme_language_switch_en','README_CN.md' in (ROOT/'README.md').read_text(encoding='utf-8'))
add('readme_language_switch_cn','README.md' in (ROOT/'README_CN.md').read_text(encoding='utf-8'))

failed=[c for c in checks if not c[1]]
for name,ok,detail in checks:
    print(('PASS' if ok else 'FAIL')+'\t'+name+(('\t'+detail) if detail else ''))
print(f'\nSUMMARY\t{len(checks)-len(failed)}/{len(checks)} PASS')
sys.exit(1 if failed else 0)
