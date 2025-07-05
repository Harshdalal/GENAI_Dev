# test_api.py
import requests

# Send a sample wine record
data = {
    "features": [13.2, 1.7, 2.51, 18.5, 103, 9.4, 1.3, 0.26, 1.56, 5.0, 1.05, 3.33, 730]
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)
print("🍷 Predicted Class:", response.json())
