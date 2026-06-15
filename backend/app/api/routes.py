"""API routes for Resume Lens."""
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.parsers import pdf_parser

router = APIRouter()


@router.post("/analyze")
async def analyze(resume: UploadFile = File(...)) -> dict:
    """Accept a resume PDF and return its extracted text.

    Thin vertical slice: upload -> parse -> raw text. Scoring comes later.
    """
    filename = resume.filename or ""
    is_pdf = resume.content_type == "application/pdf" or filename.lower().endswith(".pdf")
    if not is_pdf:
        raise HTTPException(status_code=415, detail="Only PDF resumes are supported for now.")

    file_bytes = await resume.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    try:
        result = pdf_parser.extract_text(file_bytes)
    except Exception as exc:  # pdfplumber raises various errors on bad PDFs
        raise HTTPException(status_code=422, detail=f"Could not parse PDF: {exc}") from exc

    return {
        "filename": filename,
        "page_count": result.page_count,
        "char_count": len(result.cleaned_text),
        "contact": result.contact,
        "sections": result.sections,
        "raw_text": result.raw_text,
        "cleaned_text": result.cleaned_text,
    }
