from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_prediction_endpoint_returns_price():
    payload = {
        "company": "Maruti",
        "model": "Swift",
        "year": 2018,
        "km_driven": 50000,
        "fuel": "Diesel",
        "seller_type": "Individual",
        "transmission": "Manual",
        "owner": "First Owner",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    result = response.json()
    assert result["success"] is True
    assert result["currency"] == "INR"
    assert isinstance(result["predicted_price"], (int, float))
    assert result["predicted_price"] > 0


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-q"]))
