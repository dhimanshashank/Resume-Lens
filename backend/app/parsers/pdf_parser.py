"""PDF resume parsing using pdfplumber.

This is the first step of the resume pipeline: turn an uploaded PDF into raw,
extractable text. Section detection / skill extraction happen downstream.
"""
from __future__ import annotations

import io

import pdfplumber


def extract_text(file_bytes: bytes) -> dict:
    """Extract raw text and basic layout info from a PDF resume.

    Args:
        file_bytes: the raw bytes of an uploaded PDF.

    Returns:
        A dict with:
          - raw_text:   all pages joined together
          - pages:      list of per-page text (preserves page boundaries)
          - page_count: number of pages
    """
    pages: list[str] = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text() or "")

    raw_text = "\n\n".join(pages).strip()
    return {
        "raw_text": raw_text,
        "pages": pages,
        "page_count": len(pages),
    }
