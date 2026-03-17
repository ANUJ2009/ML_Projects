# 🚦 UK Road Accident Severity Prediction Dashboard

A **Machine Learning-powered interactive dashboard** built using **Streamlit** that predicts road accident severity and visualizes accident patterns across the UK.

---

## 📌 Project Overview

This project uses a real-world dataset to:

* 🔮 Predict accident severity using ML models
* 📊 Analyze accident trends
* 🌍 Visualize accident hotspots on maps
* 📈 Display feature importance and insights

It provides a **multi-page premium dashboard UI** for a complete data-driven experience.

---

## 🚀 Features

### 🔮 Prediction Module

* Predict accident severity based on:

  * Weather conditions
  * Light conditions
  * Road type
  * Speed limit
  * Urban/Rural area
* Real-time predictions with visual indicators:

  * 🟢 Slight
  * 🟠 Serious
  * 🔴 Fatal

---

### 🌍 Accident Heatmap

* Interactive map using **Folium**
* Visualizes accident density across locations
* Helps identify high-risk zones

---

### 📊 Analytics Dashboard

* Feature importance visualization
* Dataset insights
* Distribution analysis

---

### 🏠 Home Dashboard

* KPI cards:

  * Total accidents
  * Fatal cases
  * Serious cases
  * Slight cases
* Clean and modern UI

---

## 🧠 Machine Learning

* Model Used: **Random Forest Classifier**
* Preprocessing:

  * Label Encoding for categorical features
  * Missing value handling
* Evaluation:

  * Accuracy-based performance

---

## 📂 Project Structure

```
UK_Accident_Dashboard/
│
├── app.py
├── style.py
├── uk_model.pkl
├── label_encoders.pkl
├── uk_data.csv
│
└── pages/
    ├── 1_Prediction.py
    ├── 2_Map.py
    ├── 3_Analytics.py
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn**
* **Pandas & NumPy**
* **Matplotlib**
* **Folium (Maps)**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ANUJ2009/uk-accident-dashboard.git
cd uk-accident-dashboard
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib folium streamlit-folium
```

---

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📊 Dataset

Dataset used:

* UK Road Safety Dataset (Kaggle)

Contains:

* Accident severity
* Weather conditions
* Road type
* Speed limits
* Location coordinates

---

## 💡 Future Enhancements

* 🌙 Dark/Light theme toggle
* 📍 District-level filtering
* 📊 Model comparison (XGBoost, Logistic Regression)
* 🌐 Deploy on cloud (Streamlit Cloud / Render)
* 🔐 User authentication system

---

## 🧑‍💻 Author

**Anuj Kumar**
B.Tech Student | Machine Learning Enthusiast

---

## ⭐ Acknowledgements

* Kaggle for dataset
* Streamlit for UI framework
* Scikit-learn for ML models

---

## 📬 Feedback

If you like this project, give it a ⭐ on GitHub!

---
