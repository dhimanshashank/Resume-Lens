import re, unicodedata

def clean_text(raw: str) -> str:
    text = re.sub(r"\(cid:\d+\)", "", raw)        # kill icon-font junk: (cid:131) etc.
    text = unicodedata.normalize("NFKC", text)    # ligatures, fancy quotes/dashes → ascii-ish
    text = text.replace("\u00a0", " ")            # non-breaking spaces → normal
    text = re.sub(r"[ \t]+", " ", text)           # collapse runs of spaces
    text = re.sub(r"\n{3,}", "\n\n", text)        # collapse excess blank lines
    text = "\n".join(line.strip() for line in text.splitlines())
    return text.strip()