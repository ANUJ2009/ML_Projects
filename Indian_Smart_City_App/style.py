import streamlit as st

def apply_styles():
    st.markdown("""
    <style>

    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

  /* Sidebar Container */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #1f2937);
    color: white;
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Active Page Highlight */
section[data-testid="stSidebar"] .css-1v3fvcr {
    background: linear-gradient(90deg, #00FFD1, #00B4DB);
    color: black !important;
    border-radius: 8px;
}


    }

    /* Titles */
    h1, h2, h3 {
        color: #00FFD1;
        font-weight: 700;
    }

    /* Glass Card Effect */
    .glass {
        background: rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        margin-bottom: 20px;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #00FFD1, #00B4DB);
        color: black;
        border-radius: 8px;
        font-weight: bold;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        transition: 0.2s ease-in-out;
    }

    /* Selectbox */
    div[data-baseweb="select"] {
        background-color: rgba(255,255,255,0.08);
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)
