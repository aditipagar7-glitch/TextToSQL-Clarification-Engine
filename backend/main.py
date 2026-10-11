from fastapi import FastAPI
from pydantic import BaseModel
from backend.pipeline import process_question

app = FastAPI(
    title="Text-to-SQL Clarification Engine"
)


class QuestionRequest(BaseModel):

    question: str
    clarification: str | None = None


@app.get("/")
def home():

    return {
        "message": "Text-to-SQL API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = process_question(
        request.question,
        request.clarification
    )

    return result