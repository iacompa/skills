"""Validate portable Markdown packages and measure complete source files."""
import argparse, hashlib, json, re
from pathlib import Path
import tiktoken
import yaml

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {'bilingual-business-reply':600, 'agent-permissions-audit':1200, 'lead-follow-up':800, 'review-response':550, 'project-handoff':800, 'skill-creator':1200}

def unique_object(pairs):
    result={}
    for key,value in pairs:
        if key in result: raise ValueError('Duplicate JSON key: ' + key)
        result[key]=value
    return result

def load_json(path): return json.loads(path.read_text(), object_pairs_hook=unique_object)

def validate():
    tokenizer=tiktoken.get_encoding('o200k_base')
    rows=[]
    for slug,target in TARGETS.items():
        package=ROOT/'skills'/slug
        entries=sorted(package.rglob('*'))
        files=[]
        for path in entries:
            if path.is_symlink(): raise ValueError('Symlink in package: ' + str(path))
            if path.is_dir(): continue
            relative=path.relative_to(package).as_posix()
            if not path.is_file() or not re.fullmatch(r'SKILL\.md|references/[a-zA-Z0-9_-]+\.md',relative):
                raise ValueError('Unexpected package file: ' + relative)
            files.append(relative)
        core=(package/'SKILL.md').read_text()
        if not core.startswith('---\n') or '\r' in core or not core.endswith('\n'):
            raise ValueError('Invalid source text format: ' + slug)
        parts=core.split('---\n',2)
        metadata=yaml.safe_load(parts[1])
        if set(metadata) != {'name','description'} or metadata['name'] != slug or not isinstance(metadata['description'],str) or not metadata['description'].strip():
            raise ValueError('Invalid portable frontmatter: ' + slug)
        for target_path in re.findall(r'\]\(([^)]+)\)',core):
            if ':' in target_path or target_path.startswith('/'):
                raise ValueError('Runtime source must not require a remote/absolute reference: ' + slug)
            resolved=(package/target_path.split('#')[0]).resolve()
            if not resolved.is_relative_to(package.resolve()) or not resolved.is_file():
                raise ValueError('Unresolved package reference: ' + slug)
        cases=load_json(ROOT/'evaluations/collection'/slug/'cases.json')
        expectations=load_json(ROOT/'evaluations/collection'/slug/'expectations.json')
        if len(cases)!=4 or {c['kind'] for c in cases}!={'normal','missing-conflicting','injection','consequential'}:
            raise ValueError('Four focused case kinds required: ' + slug)
        if len({c['id'] for c in cases})!=4 or {c['id'] for c in cases}!={e['id'] for e in expectations}:
            raise ValueError('Case identity mismatch: ' + slug)
        if any(set(c)!={'id','kind','request'} for c in cases):
            raise ValueError('Execution cases must not include grading criteria: ' + slug)
        catalog=load_json(ROOT/'catalogue'/f'{slug}.json')
        if catalog['slug']!=slug: raise ValueError('Catalogue mismatch')
        for key in ['name','description','overview','language','examplePrompt','exampleOutput']:
            if any(not catalog[key][lang].strip() for lang in ['en','es']): raise ValueError('Missing bilingual field: ' + slug)
        tokens=len(tokenizer.encode(core))
        rows.append({'slug':slug,'source_sha256':hashlib.sha256(core.encode()).hexdigest(),'discovery_tokens':len(tokenizer.encode(metadata['name']+'\n'+metadata['description'])),'skill_md_tokens':tokens,'target_tokens':target,'within_target':tokens<=target,'characters':len(core),'words':len(core.split()),'package_files':files,'optional_references_loaded_in_standard_workflow':0})
    return {'method':'tiktoken '+tiktoken.__version__+'; o200k_base encoding. Exact text counts for this encoding, not model-independent billing totals. Complete SKILL.md includes frontmatter. Discovery counts name + newline + description. Skill Creator has a project-selected 1200-token design target.','skills':rows}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--write',action='store_true');args=parser.parse_args()
    result=validate()
    if args.write:
        (ROOT/'evaluations/collection/measurements.json').write_text(json.dumps(result,indent=2)+'\n')
    for row in result['skills']: print(row['slug'],str(row['skill_md_tokens'])+'/'+str(row['target_tokens']),'PASS' if row['within_target'] else 'REVIEW SIZE EXCEPTION')
    print(str(len(result['skills']))+' admitted package/frontmatter/reference/catalogue/fixture checks passed.')
