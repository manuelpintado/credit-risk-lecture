import numpy as np
import json


class LinearRegression:

    def __init__(self, target_column, add_intercept, data):
        self.data = data
        self.target_column = target_column
        self.add_intercept = add_intercept
        self.X = None
        self.Y = None
        self.w = None
        self.predictors = None

    def to_dict(self):
        df = self.data
        if self.add_intercept and self.add_intercept not in df.columns:
            df[self.add_intercept] = 1
        return {
            "target_column": self.target_column,
            "add_intercept": self.add_intercept,
            "predictors": [
                column for column in df.columns if column != self.target_column
            ],
            "weights": [
                self.w.item(i) for i in range(0, len(self.w))
            ]
        }

    def train(self):
        df = self.data
        if self.add_intercept and self.add_intercept not in df.columns:
            df[self.add_intercept] = 1
        Y = np.array(df[self.target_column].values).transpose()
        self.Y = Y[:, None]
        self.X = np.array(df[[column for column in df.columns if column != self.target_column]])
        self.w = np.linalg.inv(self.X.transpose().dot(self.X)).dot(self.X.transpose()).dot(Y)
        return self

    def predict(self, data):
        df = data
        if self.add_intercept and self.add_intercept not in df.columns:
            df[self.add_intercept] = 1
        self.X = np.array(df[[column for column in df.columns if column != self.target_column]])
        pred = self.X.dot(self.w)
        return pred

    @staticmethod
    def load(filename):
        with open(filename, "r") as file:
            data = json.loads(file.read())
        return data

    def save(self, path):
        with open(path, 'w') as f:
            json.dump(self.to_dict(), f)
