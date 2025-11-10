import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join("Artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self, available_columns):
        """
        Creates a preprocessing pipeline that is robust to missing columns.
        """
        try:
            logging.info("🔧 Creating preprocessing pipeline...")

            numerical_columns = [
                "screen_size(inch)",
                "battery(mAh)",
                "storage(GB)",
                "ram(GB)",
                "selfie_camera(MP)"
            ]

            categorical_columns = [
                "brand",
                "display",
                "sim_card",
                "os",
                "color",
                "region",
                "resolution",
                "sd_card",
                "location"
            ]

            # Keep only valid columns
            valid_num_cols = [col for col in numerical_columns if col in available_columns]
            valid_cat_cols = [col for col in categorical_columns if col in available_columns]

            logging.info(f"✅ Numerical columns used: {valid_num_cols}")
            logging.info(f"✅ Categorical columns used: {valid_cat_cols}")

            if not valid_num_cols and not valid_cat_cols:
                raise CustomException("❌ No valid columns found for transformation!", sys)

            # Pipelines
            num_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(handle_unknown="ignore")),
                ("scaler", StandardScaler(with_mean=False))
            ])

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, valid_num_cols),
                ("cat_pipeline", cat_pipeline, valid_cat_cols)
            ])

            logging.info("✅ Preprocessor pipeline created successfully.")
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        """
        Reads data, applies preprocessing, and returns processed arrays along with preprocessor path.
        """
        try:
            # Load CSVs or accept DataFrame input
            if isinstance(train_path, str):
                train_df = pd.read_csv(train_path)
                test_df = pd.read_csv(test_path)
            else:
                train_df = train_path.copy()
                test_df = test_path.copy()

            logging.info("✅ Read train and test data successfully.")
            target_column_name = "price(¢)"

            if target_column_name not in train_df.columns:
                raise CustomException(
                    f"Target column '{target_column_name}' not found. Found columns: {train_df.columns.tolist()}",
                    sys
                )

            # Split input and target
            input_train_df = train_df.drop(columns=[target_column_name])
            target_train = train_df[target_column_name].values.reshape(-1, 1)

            input_test_df = test_df.drop(columns=[target_column_name])
            target_test = test_df[target_column_name].values.reshape(-1, 1)

            logging.info(f"📊 Columns in training data: {input_train_df.columns.tolist()}")

            # Create preprocessing object
            preprocessor = self.get_data_transformer_object(input_train_df.columns.tolist())

                        # Transform features
            input_train_arr = preprocessor.fit_transform(input_train_df)
            input_test_arr = preprocessor.transform(input_test_df)
            # Transform features
            input_train_arr = preprocessor.fit_transform(input_train_df)
            input_test_arr = preprocessor.transform(input_test_df)

            # If sparse matrix, convert to dense
            if hasattr(input_train_arr, "toarray"):
                input_train_arr = input_train_arr.toarray()
            if hasattr(input_test_arr, "toarray"):
                input_test_arr = input_test_arr.toarray()

            # Ensure arrays are 2D (target already reshaped)
            train_arr = np.concatenate((input_train_arr, target_train), axis=1)
            test_arr = np.concatenate((input_test_arr, target_test), axis=1)



            # Save preprocessor
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocessor)
            logging.info("💾 Preprocessing object saved successfully.")
            logging.info(f"✅ Final train_arr shape: {train_arr.shape}")
            logging.info(f"✅ Final test_arr shape: {test_arr.shape}")

            return train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path

        except Exception as e:
            raise CustomException(e, sys)
