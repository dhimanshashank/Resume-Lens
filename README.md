# Resume Lens

> **AI Resume–Job Match Analyzer** — estimates how well a resume aligns with a target job description, highlights missing skills and ATS-style issues, and suggests improvements.
>
> ⚠️ This tool estimates resume–job alignment and highlights improvement areas. It does **not** make hiring decisions, guarantee interview selection, or claim to be a real ATS.

_Status: early development — Phase 1 (parsing) in progress._

---

## What it does

Upload a **resume** (PDF / DOCX / text) and paste a **job description**, and get back:

- Overall match score out of 100 (deterministic + explainable, **not** LLM-generated)
- Breakdown: skills, keyword, semantic relevance, experience, ATS formatting
- Matched skills + missing required skills
- ATS formatting / readability warnings
- Resume improvement suggestions (and optional bullet rewrites)

## Design principle

A **deterministic scoring backbone** with a **non-trivial LLM layer** on top.
The LLM never generates the score. It is used only to: structure messy JDs (function calling),
explain the score in plain language, and rewrite bullets — strictly from detected gaps, never inventing skills.

## Scoring weights (MVP assumptions — tunable, not ground truth)

| Component          | Weight |
| ------------------ | ------ |
| Required skills    | 35%    |
| Semantic relevance | 20%    |
| Keyword similarity | 15%    |
| Preferred skills   | 10%    |
| Experience match   | 10%    |
| ATS formatting     | 10%    |

## Roadmap

**Phase 1 — NLP core (MVP):** PDF/DOCX parsing → section detection → skill extraction
(taxonomy + alias map) → keyword (TF-IDF + cosine) & semantic (embeddings API) matching →
score engine → ATS checker → score dashboard.

**Phase 2 — LLM layer:** structured JD parsing via function calling, bullet rewrite assistant,
RAG-style gap explainer reasoning over the score breakdown, prompt engineering with evaluation.

**Later:** keyword heatmap, must-have vs nice-to-have classifier, analysis history,
skill-gap → LMS course recommendations, human-labeled eval dataset.

## Tech stack

- **Backend:** FastAPI · Python · PostgreSQL · `uv`
- **Frontend:** Next.js · React · Tailwind CSS
- **NLP/ML:** pdfplumber · scikit-learn (TF-IDF/cosine) · embeddings API · LLM API (Phase 2)
- **Deploy (planned):** Render/Railway/Fly.io (backend) · Vercel (frontend)

## Project structure

```
Resume-Lens/
├── backend/          # FastAPI app
│   └── app/
│       ├── api/      # routes
│       ├── models/   # pydantic schemas
│       └── parsers/  # pdf / docx / section parsers
└── frontend/         # Next.js app
```

## Getting started

> _TODO: fill in once the first endpoint is wired._

```bash
# backend
cd backend
uv sync
uv run python main.py   # serves on http://localhost:8000

# frontend
cd frontend
npm install
npm run dev
```
