# 📱 Phone Price Prediction App

~~~ 
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange?logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24-blue?logo=docker&logoColor=white)
~~~

---

## Problem Statement

The Ghanaian smartphone market is highly dynamic, with prices varying significantly based on features such as brand, RAM, storage, battery, camera, display type, and location. Consumers, retailers, and resellers often face **uncertainty in pricing**, which can lead to **overpayment, undervaluation, or poor investment decisions**.  

This project aims to **solve the problem of price uncertainty** by building a **machine learning model** that predicts smartphone prices accurately based on specifications. By leveraging a Ghana-based dataset of phone prices, this model:

- Helps buyers make informed decisions about fair pricing.
- Assists sellers and retailers in pricing their inventory competitively.
- Supports analysts in understanding feature-price relationships in the Ghanaian market.

---

## Project Overview

The **Phone Price Prediction App** is a full-stack machine learning application that:

- Uses a **preprocessing pipeline** to handle numerical and categorical features.
- Trains a **CatBoost Regressor** model for accurate price prediction.
- Provides an **interactive Streamlit interface** for users to input phone specifications and get price predictions in real-time.
- Can be deployed **locally, via Docker, or on Streamlit Cloud**.

---

## Features

~~~
- Predict phone prices using 14+ specifications: brand, RAM, storage, battery, selfie camera, display type, region, location, etc.
- Preprocessing pipeline includes scaling numerical features and encoding categorical features.
- Supports multiple Ghanaian phone brands and specifications.
- Interactive sidebar input via Streamlit for a user-friendly experience.
- Deployable on Docker or Streamlit Cloud for easy access.
~~~

---

## Project Structure

~~~bash
Phone_prices_mlops/
│
├── Artifacts/                  
│   ├── model.pkl               # Trained CatBoost model
│   ├── preprocessor.pkl        # Preprocessing pipeline for transforming input
│   ├── train_data.csv          # Training dataset
│   ├── test_data.csv           # Testing dataset
│   └── data.csv                # Raw dataset
│
├── notebook/                  
│   └── Phone_prices_Cleaned.csv # Cleaned Ghana phone dataset
│
├── src/
│   ├── components/             
│   │   ├── data_ingestion.py      # Loads raw data, splits into train/test
│   │   ├── data_transformation.py # Preprocessing pipelines for features
│   │   └── model_trainer.py       # Model training, evaluation, saving
│   │
│   ├── pipeline/               
│   │   └── prediction_pipeline.py # PredictionPipeline and CustomData classes
│   │
│   ├── utils.py                # Helper functions (save/load objects, model evaluation)
│   ├── logger.py               # Logging configuration
│   └── exception.py            # Custom exception handling
│
├── requirements.txt            # Python dependencies
├── app.py                      # Streamlit app
└── Dockerfile                  # Docker configuration
~~~

**Explanation:**  
- `Artifacts/` stores all intermediate and final outputs like models and datasets.  
- `src/components/` contains the ML pipeline modules: ingestion, transformation, training.  
- `src/pipeline/` holds prediction-related code for deployment.  
- `utils.py`, `logger.py`, and `exception.py` support code modularity and error handling.  
- `app.py` is the front-end Streamlit interface.  
- `Dockerfile` allows containerized deployment.

---

## Setup Instructions

### 1️⃣ Clone the repository

~~~bash
git clone <your-repo-url>
cd Phone_prices_mlops
~~~

### 2️⃣ Create a virtual environment (optional)

~~~bash
python -m venv myenv
source myenv/bin/activate      # Linux/Mac
myenv\Scripts\activate         # Windows
~~~

### 3️⃣ Install dependencies

~~~bash
pip install -r requirements.txt
~~~

---

## Running Locally

~~~bash
streamlit run app.py
~~~

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Using Docker

~~~bash
docker build -t phone-price-prediction .
docker run -p 8501:8501 phone-price-prediction
~~~

Access the app at [http://localhost:8501](http://localhost:8501).

---

## Deployment on Streamlit Cloud

~~~bash
1. Push the repository to GitHub.
2. Go to https://share.streamlit.io/
3. Click "New app" → Select your repository and branch.
4. Ensure `requirements.txt` is present.
5. Deploy → The app will have a public URL.
~~~

---

## Usage

~~~bash
1. Enter phone specifications in the Streamlit sidebar.
2. Click "Predict Price".
3. The app outputs the estimated price in Ghanaian Cedis (₵).
~~~

---

## Model Details

~~~ 
- Preprocessor: ColumnTransformer (Numerical scaling + OneHotEncoding)
- Model: CatBoost Regressor (handles categorical & numerical features without explicit encoding)
- Dataset: Ghana-based phone price dataset
- Performance: R^2 score > 0.9 on test set
~~~

---


## 📹 Video Demo

![Streamlit Demo](videos/streamlit_demo.gif)

---

## Acknowledgements

~~~ 
- Ghana-based phone price dataset
- Python, Pandas, Scikit-learn, CatBoost, Streamlit
- Inspired by real-world MLOps deployment practices
~~~

---

## Contact

~~~ 
Email: alhassanabubakarjnr@gmail.com
GitHub: https://github.com/AlhassanAbubakarJnr
~~~

> 