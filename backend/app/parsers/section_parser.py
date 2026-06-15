SECTION_ALIASES = {
    "summary":        ["summary", "objective", "profile", "about"],
    "skills":         ["skills", "technical skills", "technologies"],
    "experience":     ["experience", "work experience", "employment"],
    "projects":       ["projects", "personal projects"],
    "education":      ["education", "academic background"],
    "certifications": ["certifications", "certificates", "licenses"],
}

def match_header(line: str):
    s = line.strip().lower().rstrip(":")
    if len(s.split()) > 4:
        return None
    for canon, aliases in SECTION_ALIASES.items():
        if s in aliases:
            return canon
    return None

def split_sections(text: str) -> dict[str, str]:
    sections, current = {}, "header"   # lines before 1st header = contact/name preamble
    buckets = {current: []}
    for line in text.splitlines():
        canon = match_header(line)     # returns "skills" / None
        if canon:
            current = canon
            buckets.setdefault(current, [])
        else:
            buckets[current].append(line)
    return {k: "\n".join(v).strip() for k, v in buckets.items()}