from pydantic import BaseModel, Field


class ContactInfo(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    links: dict[str, str | None] = Field(default_factory=dict)


class ParsedResume(BaseModel):
    contact: ContactInfo
    sections: dict[str, str]
    raw_text: str
    cleaned_text: str
    page_count: int