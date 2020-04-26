# To run the code you can use the following commands:
## Setup

Open this project on PyCharm and do the following:

1. Create and activate a virtualenv
    * **Use PyCharm** or one of the following:
        * `virtualenv --python=python3 venv`
        * `python3 -m virtualenv --python=python3 venv`
        * Note: you might have to use the complete python path.
    * Activate your virtual environment:
        * Mac/Linux: `source venv/bin/activate`
        * Windows: `source venv/Scripts/activate`

1. Install requirements
    * `pip install -r requirements.txt`
    
## Usage
1. To train the model

    * `$ python main.py train_linear_regression --data_path data/weight-height.csv --target_column weight --add_intercept bias --save_path data/weight_model.json`

      * data_path: `path were the information is found`
      * target_column: `column from the data set that you want to predict`
      * add_intercept:  `column for a bias; if the column is not in the data set a new one will be generated`
      * save_path: `path for the model to be saved`

1. To use the model
    * `$ python main.py score_linear_regression --model_path data/weight_model.json --data_path data/weight-height.csv --prediction weight --save_output weight_predict.csv`
      * model_path: `path where the model with the weights is saved`
      * data_path: `path for the information to be used`
      * prediction: `column to predict`
      * save_output: `path to save the predicted information`
      