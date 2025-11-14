import requests

if __name__ == "__main__":
    url = "http://localhost:9696/predict"
    client = {"age": 27, "pclass": "middle", "sex": "male", "solo": 1}
    response = requests.post(url, json=client).json()
    print(response)
