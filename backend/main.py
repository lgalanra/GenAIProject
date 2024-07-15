from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from backend.utils import dataset, nlp

app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Gen AI RAG Application"}

@app.post("/ask/")
def ask_question(question: Question):
    query = question.question
    context = " ".join(dataset['context'][:90])  # Simplified context extraction
    result = nlp(question=query, context=context)
    if result:
        return {"answer": result['answer']}
    else:
        raise HTTPException(status_code=404, detail="Answer not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
