import joblib


# Load model
model = joblib.load("CarPricePredictor.pkl")


print("=" * 60)
print("MODEL INFORMATION")
print("=" * 60)


print("\nModel type:")
print(type(model))


print("\nPipeline steps:")
print(model.named_steps.keys())


# Get preprocessor
preprocessor = model.named_steps["preprocessor"]


print("\nInput features:")
print(preprocessor.feature_names_in_)


print("\n" + "=" * 60)
print("CATEGORICAL CATEGORIES")
print("=" * 60)


encoder = preprocessor.named_transformers_["categories"]


for column, categories in zip(
    [
        "company",
        "model",
        "fuel",
        "seller_type",
        "transmission",
        "owner"
    ],
    encoder.categories_
):

    print("\n" + column)
    print("-" * 40)

    print(categories)
