import joblib
import pandas as pd

# Load model
model = joblib.load("CarPricePredictor.pkl")

# Test car
car = pd.DataFrame({
    "company": ["Maruti"],
    "model": ["Swift"],
    "fuel": ["Diesel"],
    "seller_type": ["Individual"],
    "transmission": ["Manual"],
    "owner": ["First Owner"],
    "year": [2018],
    "km_driven": [50000]
})

# Predict
prediction = model.predict(car)

print("=" * 60)
print("CAR PRICE MODEL TEST")
print("=" * 60)

print("\nRaw model prediction:")
print(prediction[0])

print("\nPrediction × 100000:")
print(prediction[0] * 100000)

print("\nPrediction × 1000:")
print(prediction[0] * 1000)
