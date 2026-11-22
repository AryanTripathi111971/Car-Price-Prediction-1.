import joblib
import pandas as pd
import sklearn


MODEL_PATH = "CarPricePredictor.pkl"

print("=" * 70)
print("MODEL DIAGNOSIS")
print("=" * 70)

print("\nScikit-learn version:")
print(sklearn.__version__)

# The saved artifact is a TransformedTargetRegressor wrapping a Pipeline.
model = joblib.load(MODEL_PATH)
pipeline = model.regressor_

print("\nModel type:")
print(type(model))

print("\nPipeline steps:")
for name, step in pipeline.named_steps.items():
    print(f"{name} -> {type(step)}")

preprocessor = pipeline.named_steps["preprocessor"]

print("\nInput features:")
print(preprocessor.feature_names_in_)

encoder = preprocessor.named_transformers_["categories"]
categorical_columns = [
    "company",
    "model",
    "fuel",
    "seller_type",
    "transmission",
    "owner",
]

print("\nCategorical columns and categories:")
for column, categories in zip(categorical_columns, encoder.categories_):
    print(f"\n{column}")
    print("-" * 50)
    print(categories)

numerical_transformer = preprocessor.named_transformers_["numerical"]
print("\nNumerical transformer:")
print(numerical_transformer)

car = pd.DataFrame(
    {
        "company": ["Maruti"],
        "model": ["Swift"],
        "fuel": ["Diesel"],
        "seller_type": ["Individual"],
        "transmission": ["Manual"],
        "owner": ["First Owner"],
        "year": [2018],
        "km_driven": [50000],
    }
)

print("\nTest input:")
print(car)

prediction = float(model.predict(car)[0])
print("\nPredicted price (INR):")
print(round(prediction, 2))

ridge = pipeline.named_steps["ridge"]
print("\nRidge regression coefficient count:")
print(len(ridge.coef_))
print("\nIntercept:")
print(ridge.intercept_)

print("\nMODEL DIAGNOSIS COMPLETED")
