
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.summarizer import summarize_text
from app.database import create_db, get_session, Summary

app = FastAPI(title="AI Text Summarizer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.on_event("startup")
def on_startup():
    create_db()

@app.get("/")
def health():
    return {"status": "Backend running"}

@app.post("/summarize")
def summarize(req: TextRequest):
    summary = summarize_text(req.text)

    with get_session() as session:
        record = Summary(
            input_text=req.text,
            summary_text=summary
        )
        session.add(record)
        session.commit()

    return {"summary": summary}


