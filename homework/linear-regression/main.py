import fire
import logging
from models import LinearRegression
import pandas as pd

logger = logging.getLogger(__name__)


class Main(object):

    @staticmethod
    def train_linear_regression(data_path: str, target_column: str, add_intercept: str = "", save_path: str = ""):
        data = pd.read_csv(data_path)
        model = LinearRegression(data=data, target_column=target_column, add_intercept=add_intercept).train()
        if save_path:
            LinearRegression.save(model, path=save_path)
        return model.to_dict()

    @staticmethod
    def score_linear_regression(model_path: str, data_path: object = None, prediction: str = "estimation",
                                save_output: str = ""):
        loaded_model = LinearRegression.load(model_path)
        if data_path:
            data = pd.read_csv(data_path)
        else:
            data = loaded_model["data"]
        model = LinearRegression(data=data, target_column=loaded_model["target_column"],
                                 add_intercept=loaded_model["add_intercept"]).train()
        pred = model.predict(data)
        data[prediction] = pred
        if save_output.endswith("csv"):
            data.to_csv(save_output)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    fire.Fire(Main)