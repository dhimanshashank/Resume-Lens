"""PDF resume parsing using pdfplumber.

This is the first step of the resume pipeline: turn an uploaded PDF into raw,
extractable text. Section detection / skill extraction happen downstream.
"""
from __future__ import annotations

import io

import pdfplumber

from .section_parser import split_sections
from .text_cleaner import clean_text
from .contact_extractor import extract_contact
from app.models.schemas import ParsedResume


def extract_text(file_bytes: bytes) -> ParsedResume:
    pages: list[str] = []

    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text() or "")

    raw_text = "\n\n".join(pages).strip()
    cleaned_text = clean_text(raw_text)

    sections = split_sections(cleaned_text)

    contact = extract_contact(
        header=sections.get("header", ""),
        full_text=cleaned_text,
    )

    return ParsedResume(
        contact=contact,
        sections=sections,
        raw_text=raw_text,
        cleaned_text=cleaned_text,
        page_count=len(pages),
    )