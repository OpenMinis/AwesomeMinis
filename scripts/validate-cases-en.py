from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
case_root=root/'cases-en'
errors=[]
mds=[p for p in case_root.rglob('*.md') if p.name not in ('README.md','SKILLS-COMPATIBILITY.md')]
for p in mds:
    s=p.read_text()
    CAND_ALLOW=re.compile(r'Original sharer:|Shared by|shared by|Screenshot by|contributor|Contributor')
    s_filtered='\n'.join(l for l in s.splitlines() if not CAND_ALLOW.search(l))
    if re.search(r'[\u3400-\u9fff]',s_filtered): errors.append(f'CJK: {p}')
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
