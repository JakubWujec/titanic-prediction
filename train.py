#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier


def train(df_train, y_train, features, **model_params):
    dicts = df_train[features].to_dict(orient="records")

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = DecisionTreeClassifier(**model_params)
    model.fit(X_train, y_train)

    return dv, model


def predict(df, dv, model, features):
    dicts = df[features].to_dict(orient="records")

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


if __name__ == "__main__":
    # parameters
    RANDOM_STATE = 34
    output_file = "model.bin"

    # data preparation
    df = pd.read_csv("data/clean_train.csv")

    numerical_features = ["age"]
    categorical_features = ["pclass", "sex", "solo"]

    df_train, df_test = train_test_split(df, test_size=0.2, random_state=RANDOM_STATE)

    y_train = df_train["survived"].values
    y_val = df_test["survived"].values

    del df_train["survived"]
    del df_test["survived"]

    features = numerical_features + categorical_features
    model_params = {"max_depth": 5, "min_samples_leaf": 6}
    dv, model = train(df_train, y_train, features, **model_params)

    y_pred = predict(
        df_test,
        dv,
        model,
        features,
    )

    auc = roc_auc_score(y_val, y_pred)
    print(auc)

    # Save the model

    with open(output_file, "wb") as f_out:
        pickle.dump((dv, model), f_out)

    print(f"the model is saved to {output_file}")
