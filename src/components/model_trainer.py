import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from src.utils import evaluate_models
# from src.components import data_transformation
import os
import sys
from dataclasses import dataclass
# from data_ingestion import DataIngestion
from src.utils import save_object


@dataclass
class ModelTrainerConfig:
    train_model_path = os.path.join("Artifacts","model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_trainer(self, train_array, test_array, preprocessor_path=None):
        logging.info("Splitting the training and test data")
        try:
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "KNN": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(random_state=42),
                "XGBRegressor": XGBRegressor(eval_metric='rmse'),
                "CatBoost": CatBoostRegressor(verbose=False, random_state=42),
                "AdaBoost": AdaBoostRegressor(random_state=42)
            }

            model_report = evaluate_models(
                X_train=X_train, y_train=y_train,
                X_test=X_test, y_test=y_test,
                models=models
            )

            best_model_score = max(model_report.values())
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No model found with acceptable performance")

            logging.info(f"Best model: {best_model_name} | R² Score: {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.train_model_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)

            # ✅ Make sure this line is correctly indented:
            return r2_square

        except Exception as e:
            raise CustomException(e, sys)
