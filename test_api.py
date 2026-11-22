import requests


url = "http://127.0.0.1:8000/predict"


data = {
    "company": "Maruti",
    "model": "Swift",
    "year": 2018,
    "km_driven": 50000,
    "fuel": "Diesel",
    "seller_type": "Individual",
    "transmission": "Manual",
    "owner": "First Owner"
}


response = requests.post(
    url,
    json=data
)


print("Status Code:")
print(response.status_code)


print("\nResponse:")
print(response.json())
