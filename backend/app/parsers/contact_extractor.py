import re


EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"\+?\d[\d\s\-()]{8,}\d")
LINKEDIN = re.compile(r"linkedin\.com/\S+", re.I)
GITHUB = re.compile(r"github\.com/\S+", re.I)
WEBSITE = re.compile(
    r"\b(?!linkedin\.com|github\.com)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
    re.I,
)


def _first(pattern: re.Pattern, text: str) -> str | None:
    match = pattern.search(text)
    return match.group().strip() if match else None


def extract_contact(header: str, full_text: str) -> dict:
    name = next((line.strip() for line in header.splitlines() if line.strip()), None)

    return {
        "name": name,
        "email": _first(EMAIL, full_text),
        "phone": _first(PHONE, full_text),
        "links": {
            "linkedin": _first(LINKEDIN, full_text),
            "github": _first(GITHUB, full_text),
        },
        "website": _first(WEBSITE, full_text)
    }