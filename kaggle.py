import pickle
import pandas as pd


def main():
    print("Hello from titanic-prediction!")


def predict(df, dv, model, features):
    dicts = df[features].to_dict(orient="records")

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


if __name__ == "__main__":
    model_file = "model.bin"

    with open(model_file, "rb") as f_in:
        dv, model = pickle.load(f_in)

    df_test = pd.read_csv("./data/clean_test.csv")

    features = numerical_features = ["age", "pclass", "sex", "solo"]

    y_pred = predict(df_test, dv, model, features)
    df_test["Survived"] = (y_pred > 0.5).astype(int)
    df_test = df_test.rename(columns={"passengerid": "PassengerId"})

    df_test = df_test[["PassengerId", "Survived"]]

    df_test.to_csv("./data/kaggle.csv", index=False)
