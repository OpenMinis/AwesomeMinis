from pathlib import Path
import re
root=Path('/var/minis/workspace/AwesomeMinis_pr')
case_root=root/'cases-en'
errors=[]
mds=[p for p in case_root.rglob('*.md') if p.name not in ('README.md','SKILLS-COMPATIBILITY.md')]
for p in mds:
    s=p.read_text()
    if re.search(r'[\u3400-\u9fff]',s): errors.append(f'CJK: {p}')
    first=next((x for x in s.splitlines() if x.strip()),'')
    if not first.startswith('# '): errors.append(f'H1: {p}')
    for url in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s):
        if '://' in url: continue
        # English cases intentionally reuse the repository's root assets directory.
        target=(p.parent/url).resolve()
        if not target.exists(): errors.append(f'image: {p} -> {url}')
print('case_files',len(mds))
print('errors',len(errors))
for e in errors: print(e)
raise SystemExit(bool(errors))
