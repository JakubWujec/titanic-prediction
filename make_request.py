import requests

if __name__ == "__main__":
    url = "http://localhost:9696/api/predict"
    client = {"age": 2, "pclass": "lower", "sex": "male", "solo": 0}
    response = requests.post(url, json=client).json()
    print(response)
