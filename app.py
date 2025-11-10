# =========================================================
# 📱 Phone Price Prediction Streamlit App
# =========================================================
import os
import pandas as pd
import streamlit as st
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomData

# ------------------ App Title ------------------
st.title("📱 Phone Price Prediction App")
st.write("Predict smartphone prices based on specifications using a trained ML model.")

# ------------------ Sidebar Inputs ------------------
st.sidebar.header("🔧 Enter Phone Specifications")

def user_input_features():
    brand = st.sidebar.selectbox("Brand", 
        ['Samsung','Tecno','LG','Vivo','Huawei','Infinix','Apple','Google','Oppo',
         'Nokia','Other Brand','Itel','Motorola','Xiaomi','OnePlus'])

    sd_card = st.sidebar.selectbox("SD Card Support", ['Yes', 'No'])
    resolution = st.sidebar.selectbox("Resolution", 
        ['1440 x 3040','1440 x 3088','1080 x 2340','1080 x 2400','Others',
         '1080 x 2460','1440 x 2880','1440 x 3200','1440 x 2960','720 x 1600',
         '1284 x 2778','1440 x 2560','1080 x 1920','1440 x 3120','1242 x 2688'])

    display = st.sidebar.selectbox("Display Type", 
        ['AMOLED','Super AMOLED','IPS LCD','P-OLED','IPS','OLED','TFT','PLS LCD',
         'Super Retina OLED','Retina IPS LCD','G-OLED','P-OLED+','PLS',
         'Monochrome','Super LCD3','Dynamic AMOLED','TN','Retina IPS',
         'Dynamic AMOLED / Dynamic AMOLED'])

    sim_card = st.sidebar.selectbox("SIM Type", ['Single','Dual','Nano-SIM'])
    os_type = st.sidebar.selectbox("Operating System", ['Android','IOS','Others'])
    color = st.sidebar.selectbox("Color", 
        ['White','Bronze','Black','Blue','Green','Silver','Gold','Gray','Pink',
         'Yellow','Other','Rose Gold','Purple','Red','Orange'])
    region = st.sidebar.selectbox("Region", ["Greater Accra","Ashanti","Eastern"])
    location = st.sidebar.selectbox("Location",
        ['Circle','Accra Metropolitan','Kokomlemle','Others','Kumasi Metropolitan',
         'Adabraka','Achimota','Labone','Dansoman','East Legon','Madina','Lapaz',
         'Adenta','Ablekuma','Labadi','Abelemkpe','Tema Metropolitan','Adjiriganor',
         'Osu','Cantonments','Dworwulu','Darkuman','Kaneshie','Bubuashie','Santa Maria'])

    screen_size = st.sidebar.number_input("Screen Size (in inches)", min_value=3.0, max_value=10.0, value=6.0, step=0.1)
    battery = st.sidebar.number_input("Battery Capacity (mAh)", min_value=1000, max_value=10000, value=4000, step=100)
    storage = st.sidebar.number_input("Storage (GB)", min_value=8, max_value=1024, value=128, step=8)
    ram = st.sidebar.number_input("RAM (GB)", min_value=1, max_value=256, value=8, step=1)
    selfie_cam = st.sidebar.number_input("Selfie Camera (MP)", min_value=1, max_value=200, value=16, step=1)

    return CustomData(
        brand=brand,
        sd_card=sd_card,
        resolution=resolution,
        display=display,
        sim_card=sim_card,
        os=os_type,
        color=color,
        region=region,
        location=location,
        screen_size_inch=screen_size,
        battery_mAh=battery,
        storage_GB=storage,
        ram_GB=ram,
        selfie_camera_MP=selfie_cam,
    )

# Collect user input
custom_data = user_input_features()
input_df = custom_data.get_data_as_data_frame()

# Display the input features
st.subheader("📋 Input Specifications")
st.write(input_df)

# ------------------ Prediction Section ------------------
if st.button("Predict Price"):
    try:
        pipeline = PredictionPipeline()
        prediction = pipeline.predict(input_df)

        st.success(f"💰 Predicted Phone Price: ₵ {float(prediction[0]):,.2f}")

    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
