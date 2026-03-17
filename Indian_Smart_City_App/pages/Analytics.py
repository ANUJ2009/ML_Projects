import streamlit as st
import pickle
import pandas as pd
from style import apply_styles

apply_styles()
st.title("📊 Feature Importance Analysis")

model = pickle.load(open("uk_model.pkl", "rb"))

features = [
    "Weather",
    "Light",
    "Road Type",
    "Speed Limit",
    "Urban/Rural"
]

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

st.markdown('<div class="glass">', unsafe_allow_html=True)
st.bar_chart(importance_df.set_index("Feature"))
st.markdown('</div>', unsafe_allow_html=True)
