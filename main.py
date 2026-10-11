
from fastapi import FastAPI

app = FastAPI(title="Student Management API")


@app.get("/")
def home():
    return {"message": "Welcome to my API"}


@app.get("/predict")
def predict_score(
    study_hours: float,
    previous_marks: float
):
    predicted_score = (
        study_hours * 5 + previous_marks * 0.8
    )

    return {
        "predicted_score": round(predicted_score, 2)
    }