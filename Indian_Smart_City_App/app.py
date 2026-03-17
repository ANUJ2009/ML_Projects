import streamlit as st
import pandas as pd
from style import apply_styles

st.set_page_config(page_title="UK Accident Dashboard", layout="wide")
apply_styles()

st.title("🚦 UK Road Accident Severity Dashboard")

df = pd.read_csv("uk_data.csv")

# KPIs
total_accidents = len(df)
fatal_cases = len(df[df["Accident_Severity"] == 1])
serious_cases = len(df[df["Accident_Severity"] == 2])
slight_cases = len(df[df["Accident_Severity"] == 3])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="glass">
        <h3>Total Accidents</h3>
        <h2>{total_accidents}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="glass">
        <h3>Fatal</h3>
        <h2>{fatal_cases}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="glass">
        <h3>Serious</h3>
        <h2>{serious_cases}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="glass">
        <h3>Slight</h3>
        <h2>{slight_cases}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
### 📊 Navigate using sidebar:
- 🔮 Prediction
- 🌍 Heatmap
- 📈 Analytics
""")
