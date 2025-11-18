import pickle

from flask import Flask, redirect, render_template, url_for
from flask import request
from flask import jsonify


model_file = "model.bin"

with open(model_file, "rb") as f_in:
    dv, model = pickle.load(f_in)

app = Flask("survive")


def make_prediction(passenger):
    X = dv.transform([passenger])
    y_pred = model.predict_proba(X)[0, 1]
    survived = y_pred >= 0.5

    return {"p": float(y_pred), "survived": bool(survived)}


@app.route("/api/predict", methods=["GET", "POST"])
def api_predict():
    passenger = request.get_json()
    result = make_prediction(passenger)
    return jsonify(result)


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        age = request.form["age"]
        pclass = request.form["pclass"]
        sex = request.form["sex"]
        solo = request.form["solo"]
        passenger = {"age": age, "pclass": pclass, "sex": sex, "solo": solo}

        result = make_prediction(passenger)
        return redirect(
            url_for("show_result", p=result["p"], survived=result["survived"])
        )

    return render_template("form.html")


@app.route("/result")
def show_result():
    survived = request.args.get("survived", type=bool)
    p = request.args.get("p", type=float)

    if survived is None or p is None:
        return redirect(
            url_for(
                "/",
            )
        )

    return render_template("result.html", p=p, survived=survived)


@app.route("/ping", methods=["GET"])
def ping():
    return "PONG"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
