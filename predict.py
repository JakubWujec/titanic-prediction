import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = "model.bin"

with open(model_file, "rb") as f_in:
    dv, model = pickle.load(f_in)

app = Flask("survive")


@app.route("/predict", methods=["POST"])
def predict():
    passenger = request.get_json()

    X = dv.transform([passenger])
    y_pred = model.predict_proba(X)[0, 1]
    survive = y_pred >= 0.5

    result = {"survive_probability": float(y_pred), "survive": bool(survive)}

    return jsonify(result)


@app.route("/ping", methods=["GET"])
def ping():
    return "PONG"


if __name__ == "__main__":
    print(app)
    app.run(debug=True, host="0.0.0.0", port=9696)
