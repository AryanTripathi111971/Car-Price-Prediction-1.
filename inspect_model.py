import joblib


MODEL_PATH = "CarPricePredictor.pkl"

# The saved artifact is a TransformedTargetRegressor wrapping a Pipeline.
model = joblib.load(MODEL_PATH)
pipeline = model.regressor_

print("=" * 60)
print("MODEL INFORMATION")
print("=" * 60)

print("\nModel type:")
print(type(model))

print("\nPipeline steps:")
print(pipeline.named_steps.keys())

preprocessor = pipeline.named_steps["preprocessor"]

print("\nInput features:")
print(preprocessor.feature_names_in_)

print("\nCategorical categories:")
encoder = preprocessor.named_transformers_["categories"]

categorical_columns = [
    "company",
    "model",
    "fuel",
    "seller_type",
    "transmission",
    "owner",
]

for column, categories in zip(categorical_columns, encoder.categories_):
    print(f"\n{column}")
    print("-" * 40)
    print(categories)

print("\nRegression estimator:")
print(pipeline.named_steps["ridge"])
