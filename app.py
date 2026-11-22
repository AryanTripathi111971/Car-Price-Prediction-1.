from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "CarPricePredictor.pkl"

# Load the trained scikit-learn pipeline once when the API starts.
model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Car Price Prediction API",
    description="Estimate the resale price of a used car from its details.",
    version="1.0.0",
)

# Permissive CORS is convenient for local development.
# Restrict allow_origins before deploying this API publicly.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CarData(BaseModel):
    company: str = Field(min_length=1)
    model: str = Field(min_length=1)
    year: int = Field(ge=1990, le=2026)
    km_driven: int = Field(ge=0)
    fuel: str = Field(min_length=1)
    seller_type: str = Field(min_length=1)
    transmission: str = Field(min_length=1)
    owner: str = Field(min_length=1)


@app.get("/")
def home():
    """Basic API health check."""
    return {"message": "Car Price Prediction API is running!"}


@app.post("/predict")
def predict_price(car: CarData):
    """Return the estimated used-car price in Indian rupees."""
    input_data = pd.DataFrame(
        [
            {
                "company": car.company.strip(),
                "model": car.model.strip(),
                "fuel": car.fuel,
                "seller_type": car.seller_type,
                "transmission": car.transmission,
                "owner": car.owner,
                "year": car.year,
                "km_driven": car.km_driven,
            }
        ]
    )

    try:
        prediction = float(model.predict(input_data)[0])
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="The model could not generate a prediction for these inputs.",
        ) from exc

    return {
        "success": True,
        "message": "Prediction successful",
        "predicted_price": round(prediction, 2),
        "currency": "INR",
    }
