import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from style import apply_styles

apply_styles()
st.title("🌍 UK Accident Heatmap")

df = pd.read_csv("uk_data.csv")

map_center = [df["Latitude"].mean(), df["Longitude"].mean()]
m = folium.Map(location=map_center, zoom_start=6)

heat_data = df[["Latitude", "Longitude"]].dropna().values.tolist()
HeatMap(heat_data, radius=8).add_to(m)

st_folium(m, width=1200)
