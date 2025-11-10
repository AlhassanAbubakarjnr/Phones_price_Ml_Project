import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictionPipeline:
    def __init__(self):
        """
        Initializes paths for model and preprocessor.
        """
        try:
            self.model_path = os.path.join("Artifacts", "model.pkl")
            self.preprocessor_path = os.path.join("Artifacts", "preprocessor.pkl")
            # self.preprocessor_path = "Artifacts\preprocessor.pkl"
            self.model = load_object(file_path=self.model_path)
            self.preprocessor = load_object(file_path=self.preprocessor_path)

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features: pd.DataFrame):
        """
        Transforms input features and returns predicted price.
        """
        try:
            if self.preprocessor is None:
                raise ValueError("Preprocessor object is not loaded. Please check the file path.")
            if self.model is None:
                raise ValueError("Model object is not loaded. Please check the file path.")

            data_scaled = self.preprocessor.transform(features)
            preds = self.model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    """
    This class maps user input fields into a pandas DataFrame
    matching the training data schema for prediction.
    """

    def __init__(
        self,
        brand: str,
        sd_card: str,
        resolution: str,
        display: str,
        sim_card: str,
        os: str,
        color: str,
        region: str,
        location: str,
        screen_size_inch: float,
        battery_mAh: float,
        storage_GB: float,
        ram_GB: float,
        selfie_camera_MP: float,
    ):
        self.brand = brand
        self.sd_card = sd_card
        self.resolution = resolution
        self.display = display
        self.sim_card = sim_card
        self.os = os
        self.color = color
        self.region = region
        self.location = location
        self.screen_size_inch = screen_size_inch
        self.battery_mAh = battery_mAh
        self.storage_GB = storage_GB
        self.ram_GB = ram_GB
        self.selfie_camera_MP = selfie_camera_MP

    def get_data_as_data_frame(self):
        """
        Converts user inputs into a pandas DataFrame
        ready for preprocessing and prediction.
        """
        try:
            custom_data_input_dict = {
                "brand": [self.brand],
                "sd_card": [self.sd_card],
                "resolution": [self.resolution],
                "display": [self.display],
                "sim_card": [self.sim_card],
                "os": [self.os],
                "color": [self.color],
                "region": [self.region],
                "location": [self.location],
                "screen_size(inch)": [self.screen_size_inch],
                "battery(mAh)": [self.battery_mAh],
                "storage(GB)": [self.storage_GB],
                "ram(GB)": [self.ram_GB],
                "selfie_camera(MP)": [self.selfie_camera_MP],
            }

            df = pd.DataFrame(custom_data_input_dict)
            return df

        except Exception as e:
            raise CustomException(e, sys)
