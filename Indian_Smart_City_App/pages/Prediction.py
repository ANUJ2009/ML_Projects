import streamlit as st
import pickle
import numpy as np
from style import apply_styles

apply_styles()
st.title("🔮 Accident Severity Prediction")

model = pickle.load(open("uk_model.pkl", "rb"))
le_dict = pickle.load(open("label_encoders (2).pkl", "rb"))

st.markdown('<div class="glass">', unsafe_allow_html=True)

weather = st.selectbox("Weather Conditions", le_dict["Weather_Conditions"].classes_)
light = st.selectbox("Light Conditions", le_dict["Light_Conditions"].classes_)
road = st.selectbox("Road Type", le_dict["Road_Type"].classes_)
urban = st.selectbox("Urban or Rural Area", le_dict["Urban_or_Rural_Area"].classes_)
speed = st.slider("Speed Limit", 20, 120, 60)

weather_enc = le_dict["Weather_Conditions"].transform([weather])[0]
light_enc = le_dict["Light_Conditions"].transform([light])[0]
road_enc = le_dict["Road_Type"].transform([road])[0]
urban_enc = le_dict["Urban_or_Rural_Area"].transform([urban])[0]

input_data = np.array([[weather_enc, light_enc, road_enc, speed, urban_enc]])

if st.button("Predict Severity"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🔴 Fatal Accident")
    elif prediction == 2:
        st.warning("🟠 Serious Accident")
    else:
        st.success("🟢 Slight Accident")

st.markdown('</div>', unsafe_allow_html=True)
