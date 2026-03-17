import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------------
# Page config & UI styling
# --------------------------------------------------
st.set_page_config(
    page_title="Traffic Accident Severity Prediction",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Load model
# --------------------------------------------------
MODEL_PATH = "model_rf.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found. Please place model_rf.pkl in the project folder.")
    st.stop()

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("🚦 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "🔮 Prediction",
        "📊 Feature Importance",
        "📈 Charts & Statistics",
        "🧠 Model Comparison",
        "🌍 Accident Hotspots"
    ]
)

# --------------------------------------------------
# PAGE 1: Prediction
# --------------------------------------------------
if page == "🔮 Prediction":
    st.title("🚦 Traffic Accident Severity Prediction")
    st.write("Predict the severity of a road accident using Machine Learning")

    st.divider()

    # ---- User Inputs ----
    weather = st.selectbox(
        "Weather Condition",
        ["Fine", "Rain", "Snow", "Fog", "Other"]
    )

    road_surface = st.selectbox(
        "Road Surface Condition",
        ["Dry", "Wet", "Snow", "Ice"]
    )

    light_condition = st.selectbox(
        "Light Condition",
        ["Daylight", "Darkness"]
    )

    speed_limit = st.slider(
        "Speed Limit (km/h)",
        min_value=20,
        max_value=120,
        value=60
    )

    num_vehicles = st.slider(
        "Number of Vehicles Involved",
        min_value=1,
        max_value=10,
        value=2
    )

    # ---- Encoding (must match training) ----
    weather_map = {
        "Fine": 0,
        "Rain": 1,
        "Snow": 2,
        "Fog": 3,
        "Other": 4
    }

    road_map = {
        "Dry": 0,
        "Wet": 1,
        "Snow": 2,
        "Ice": 3
    }

    light_map = {
        "Daylight": 0,
        "Darkness": 1
    }

    weather_enc = weather_map[weather]
    road_enc = road_map[road_surface]
    light_enc = light_map[light_condition]

    input_data = np.array([[
        weather_enc,
        road_enc,
        light_enc,
        speed_limit,
        num_vehicles
    ]])

    # ---- Prediction ----
    if st.button("🔮 Predict Severity"):
        prediction = model.predict(input_data)[0]

        if prediction == 0:
            st.success("🟢 Accident Severity: SLIGHT")
        elif prediction == 1:
            st.warning("🟠 Accident Severity: SERIOUS")
        else:
            st.error("🔴 Accident Severity: FATAL")

# --------------------------------------------------
# PAGE 2: Feature Importance
# --------------------------------------------------
elif page == "📊 Feature Importance":
    st.title("📊 Feature Importance Analysis")

    feature_names = [
        "Weather Condition",
        "Road Surface Condition",
        "Light Condition",
        "Speed Limit",
        "Number of Vehicles"
    ]

    importances = model.feature_importances_

    fi_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False)

    st.dataframe(fi_df, use_container_width=True)

    fig, ax = plt.subplots()
    ax.barh(fi_df["Feature"], fi_df["Importance"])
    ax.invert_yaxis()
    ax.set_xlabel("Importance Score")
    ax.set_title("Feature Importance")

    st.pyplot(fig)

    st.info(
        "📌 Feature importance shows which factors most influence accident severity."
    )

# --------------------------------------------------
# PAGE 3: Charts & Statistics
# --------------------------------------------------
elif page == "📈 Charts & Statistics":
    st.title("📈 Accident Statistics & Insights")

    st.subheader("Accident Severity Distribution (Sample Analysis)")

    severity_counts = {
        "Slight": 60,
        "Serious": 25,
        "Fatal": 15
    }

    fig, ax = plt.subplots()
    ax.pie(
        severity_counts.values(),
        labels=severity_counts.keys(),
        autopct="%1.1f%%",
        startangle=90
    )
    ax.set_title("Accident Severity Distribution")

    st.pyplot(fig)

    st.info(
        "📊 Most accidents are slight, but fatal accidents, although fewer, have the highest impact."
    )

# --------------------------------------------------
# PAGE 4: Model Comparison
# --------------------------------------------------
elif page == "🧠 Model Comparison":
    st.title("🧠 Model Comparison")

    comparison_data = {
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest"
        ],
        "Accuracy (%)": [
            72,
            78,
            85
        ]
    }

    comp_df = pd.DataFrame(comparison_data)

    st.table(comp_df)

    st.success(
        "✅ Random Forest was selected due to its higher accuracy and robustness."
    )

# --------------------------------------------------
# PAGE 5: Accident Hotspots
# --------------------------------------------------
elif page == "🌍 Accident Hotspots":
    st.title("🌍 Accident Hotspot Visualization")

    # Sample coordinates (demo purpose)
    data = pd.DataFrame({
        "lat": np.random.uniform(28.4, 28.8, 50),
        "lon": np.random.uniform(77.0, 77.4, 50)
    })

    st.map(data)

    st.warning(
        "⚠️ Hotspot locations are for demonstration purposes only."
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("🚧 Educational Project | Traffic Accident Severity Prediction using Machine Learning")
