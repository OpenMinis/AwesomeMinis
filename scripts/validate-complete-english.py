#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
mds=[p for p in root.rglob('*.md') if '.git' not in p.parts]
for p in mds:
 s=p.read_text(errors='replace')
 # Skip contributor attribution lines (names in original language are intentional)
 CAND_ALLOW=re.compile(r'Original sharer:|Shared by|shared by|Screenshot by|contributor|Contributor')
 s_filtered='\n'.join(l for l in s.splitlines() if not CAND_ALLOW.search(l) and not (l.strip().startswith('|') and p.name=='README.md'))
 if re.search(r'[\u3400-\u9fff]',s_filtered): errors.append(f'Chinese text remains: {p.relative_to(root)}')
 first=next((x for x in s.splitlines() if x.strip()),'')
 if not first.startswith('#'): errors.append(f'no Markdown heading: {p.relative_to(root)}')
 for target in re.findall(r'!?(?:\[[^\]]*\])\(([^)]+)\)',s):
  if target.startswith(('http://','https://','#','mailto:','minis://')) or any(x in target for x in '<>{}'): continue
  if target in ('../../assets/screenshots/your-screenshot.png','cases/category/your-file.md'): continue
  candidate=(p.parent/target.split('#',1)[0]).resolve()
  if not candidate.exists(): errors.append(f'broken local link: {p.relative_to(root)} -> {target}')
for p in root.rglob('*'):
 if '.git' not in p.parts and re.search(r'[\u3400-\u9fff]',p.name): errors.append(f'Chinese filename remains: {p.relative_to(root)}')
canonical=sorted(p.relative_to(root/'cases') for p in (root/'cases').rglob('*.md'))
translated=sorted(p.relative_to(root/'cases-en') for p in (root/'cases-en').rglob('*.md') if p.name not in ('README.md','SKILLS-COMPATIBILITY.md'))
missing=sorted(set(canonical)-set(translated))
if missing: errors.append(f'untranslated canonical cases ({len(missing)}): {missing}')
print('markdown_files',len(mds)); print('canonical_cases',len(canonical)); print('english_cases',len(translated)); print('errors',len(errors))
for e in errors: print(e)
sys.exit(1 if errors else 0)
