import numpy as np
import pandas as pd

from app import model


def test_saved_model_returns_finite_price():
    sample = pd.DataFrame(
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

    prediction = model.predict(sample)

    assert len(prediction) == 1
    assert np.isfinite(float(prediction[0]))
    assert float(prediction[0]) > 0
