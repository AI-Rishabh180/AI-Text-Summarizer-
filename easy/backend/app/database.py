
from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "summaries.db"
DB_PATH.parent.mkdir(exist_ok=True)

engine = create_engine(
    f"sqlite:///{DB_PATH}",
    connect_args={"check_same_thread": False}
)

class Summary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    input_text: str
    summary_text: str

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)


