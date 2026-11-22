import joblib
import pandas as pd
import sklearn


print("=" * 70)
print("MODEL DIAGNOSIS")
print("=" * 70)


# ==========================================================
# 1. SCIKIT-LEARN VERSION
# ==========================================================

print("\nScikit-learn version:")
print(sklearn.__version__)


# ==========================================================
# 2. LOAD MODEL
# ==========================================================

model = joblib.load("CarPricePredictor.pkl")

print("\nModel type:")
print(type(model))


# ==========================================================
# 3. PIPELINE
# ==========================================================

print("\nPipeline:")
print(model)


# ==========================================================
# 4. PIPELINE STEPS
# ==========================================================

print("\nPipeline steps:")

for name, step in model.named_steps.items():
    print(f"{name} -> {type(step)}")


# ==========================================================
# 5. PREPROCESSOR
# ==========================================================

preprocessor = model.named_steps["preprocessor"]

print("\nInput features:")
print(preprocessor.feature_names_in_)


# ==========================================================
# 6. CATEGORICAL FEATURES
# ==========================================================

encoder = preprocessor.named_transformers_["categories"]

categorical_columns = [
    "company",
    "model",
    "fuel",
    "seller_type",
    "transmission",
    "owner"
]

print("\nCategorical columns and categories:")

for column, categories in zip(
    categorical_columns,
    encoder.categories_
):

    print("\n" + column)
    print("-" * 50)
    print(categories)


# ==========================================================
# 7. NUMERICAL TRANSFORMER
# ==========================================================

numerical_transformer = (
    preprocessor.named_transformers_["Numerical_variables"]
)

print("\nNumerical transformer:")
print(numerical_transformer)


# ==========================================================
# 8. POLYNOMIAL FEATURES
# ==========================================================

poly = numerical_transformer.named_steps["poly"]

print("\nPolynomial Features:")
print("Degree:", poly.degree)


# ==========================================================
# 9. TEST CAR
# ==========================================================

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


print("\n" + "=" * 70)
print("TEST INPUT")
print("=" * 70)

print(car)


# ==========================================================
# 10. PREDICTION
# ==========================================================

prediction = model.predict(car)

raw_prediction = float(prediction[0])


print("\n" + "=" * 70)
print("PREDICTION")
print("=" * 70)

print("\nRaw model prediction:")
print(raw_prediction)

print("\nRaw prediction × 100000:")
print(raw_prediction * 100000)


# ==========================================================
# 11. MODEL COEFFICIENT INFORMATION
# ==========================================================

linear_model = model.named_steps["linear"]

print("\n" + "=" * 70)
print("LINEAR REGRESSION INFORMATION")
print("=" * 70)

print("\nNumber of coefficients:")
print(len(linear_model.coef_))

print("\nIntercept:")
print(linear_model.intercept_)


print("\n" + "=" * 70)
print("DIAGNOSIS COMPLETED")
print("=" * 70)
