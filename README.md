# Car Price Prediction

An end-to-end **used car price prediction** application built with **Python, Scikit-learn, FastAPI, HTML, CSS, and JavaScript**. Enter a vehicle's details in the web interface and receive an estimated resale price in Indian rupees (INR).

## Project overview

The application combines a trained machine-learning pipeline with a REST API and a browser-based frontend.

- **Machine learning:** Scikit-learn regression pipeline saved as `CarPricePredictor.pkl`
- **API:** FastAPI endpoint that validates vehicle details and returns a prediction
- **Frontend:** HTML, CSS, and JavaScript form with input validation, loading state, error messages, and formatted price output
- **Currency:** INR (₹)

## Features

- Predicts an estimated used-car resale price
- Accepts company, model, manufacturing year, kilometers driven, fuel type, seller type, transmission, and owner category
- Uses a FastAPI REST endpoint for model inference
- Includes frontend-side and API-side input validation
- Displays the prediction in Indian number formatting
- Includes scripts for inspecting and testing the saved model and API

## Tech stack

| Area | Technology |
|---|---|
| Language | Python |
| Machine learning | Scikit-learn |
| Data handling | Pandas |
| Model serialization | Joblib |
| Backend API | FastAPI |
| ASGI server | Uvicorn |
| Frontend | HTML, CSS, JavaScript |

## Machine-learning pipeline

The deployed artifact is a `TransformedTargetRegressor` containing a Scikit-learn pipeline. The pipeline applies:

1. **Categorical preprocessing:** `OneHotEncoder(handle_unknown="ignore")` to the company, model, fuel, seller type, transmission, and owner fields.
2. **Numerical preprocessing:** `StandardScaler` followed by `PolynomialFeatures` for year and kilometers driven.
3. **Regression:** Ridge Regression (`alpha=1`).
4. **Target transformation:** `log1p` during training and `expm1` when converting predictions back to the original target scale.

The model artifact was serialized with **Scikit-learn 1.8.0**. The requirements file pins that version to reduce pickle compatibility problems.

## Repository structure

```text
Car-Price-Prediction-1./
├── app.py
├── CarPricePredictor.pkl
├── requirements.txt
├── inspect_model.py
├── model_diagnosis.py
├── predict_test.py
├── test_api.py
├── test_model.py
├── Frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
└── .gitignore
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/AryanTripathi111971/Car-Price-Prediction-1..git
cd Car-Price-Prediction-1.
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the FastAPI backend

Run this command from the repository root:

```bash
uvicorn app:app --reload
```

The API will be available at:

- API root: http://127.0.0.1:8000/
- Interactive API documentation: http://127.0.0.1:8000/docs

### 5. Open the frontend

With the backend running, open `Frontend/index.html` in your browser. The frontend sends prediction requests to:

```text
http://127.0.0.1:8000/predict
```

Keep the backend running while using the frontend.

## API usage

### Endpoint

```http
POST /predict
Content-Type: application/json
```

### Example request

```json
{
  "company": "Maruti",
  "model": "Swift",
  "year": 2018,
  "km_driven": 50000,
  "fuel": "Diesel",
  "seller_type": "Individual",
  "transmission": "Manual",
  "owner": "First Owner"
}
```

### Example response shape

```json
{
  "success": true,
  "message": "Prediction successful",
  "predicted_price": 956594.92,
  "currency": "INR"
}
```

The numeric prediction above is an illustrative example; results depend on the included model artifact and input.

## Testing and model inspection

Run a direct model prediction:

```bash
python predict_test.py
```

Inspect the model's preprocessing pipeline and learned categorical values:

```bash
python inspect_model.py
```

Run the model diagnosis script:

```bash
python model_diagnosis.py
```

To test the HTTP endpoint, first start the API in one terminal and then run:

```bash
python test_api.py
```

## Notes and limitations

- The output is a model-based estimate, not a guaranteed market or resale price.
- Prediction quality depends on the data used to train the model and on how representative the supplied vehicle details are.
- The frontend currently targets a locally running API at `127.0.0.1:8000`.
- CORS is permissive for local development. Restrict allowed origins before deploying publicly.

## Author

**Aryan Tripathi**

GitHub: [AryanTripathi111971](https://github.com/AryanTripathi111971)
