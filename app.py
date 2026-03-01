import streamlit as st
import matplotlib.pyplot as plt
from utils import load_model, predict_churn

# Load model
model = load_model()

# Page configuration
st.set_page_config(
    page_title="AI Game Churn Predictor",
    page_icon="🎮",
    layout="centered"
)

# === Elegant Minimal CSS ===
st.markdown("""
    <style>
    body, .stApp {
        background-color: #f5f7fa;
        font-family: 'Poppins', sans-serif;
        color: #222;
    }

    /* Top Credit */
    .top-credit {
        text-align: center;
        font-size: 20px;
        font-weight: 600;
        color: #0b2545;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }

    /* Main Title */
    h1 {
        text-align: center;
        font-size: 36px !important;
        color: #102a43 !important;
        margin-bottom: 5px;
        font-weight: 700 !important;
    }

    /* Subtitle / Description */
    .description {
        text-align: center;
        color: #334e68;
        font-size: 17px;
        margin-bottom: 25px;
    }

    /* Panels */
    .panel {
        background: #ffffff;
        border-radius: 14px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }

    h2 {
        text-align: center;
        color: #0b2545 !important;
        font-size: 22px !important;
        font-weight: 600 !important;
        margin-bottom: 20px;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(90deg, #0072ff, #00c6ff);
        color: #fff;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 17px;
        transition: 0.3s ease-in-out;
        display: block;
        margin: 0 auto;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 12px rgba(0, 114, 255, 0.5);
    }

    /* Chart Section */
    .chart-panel {
        background: #ffffff;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-top: 15px;
        text-align: center;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #7b8794;
        font-size: 15px;
        margin-top: 30px;
        padding-top: 15px;
        border-top: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# === Top Credit ===
st.markdown('<div class="top-credit"> Made by <b>RUPESH PATARE</b></div>', unsafe_allow_html=True)

# === App Title ===
st.markdown("<h1>🎮 AI Game Churn Predictor</h1>", unsafe_allow_html=True)
st.markdown('<div class="description">Predict whether a player will stay loyal or churn using AI-driven analysis of gameplay behavior.</div>', unsafe_allow_html=True)

# === Input Panel ===
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown("<h2> Enter Player Details</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    sessions = st.slider("🎯 Sessions Played", 0, 500, 100)
    purchases = st.slider("💰 In-Game Purchases", 0, 50, 8)
with col2:
    session_length = st.slider("⏱ Average Session Time (minutes)", 0.0, 300.0, 75.0, step=1.0)
    level = st.slider("🏆 Player Level", 1, 100, 20)

st.markdown('</div>', unsafe_allow_html=True)

# === Prediction Section ===
if st.button("Predict Churn"):
    result = predict_churn(model, sessions, session_length, purchases, level)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("<h2> Prediction Result</h2>", unsafe_allow_html=True)

    if result == 1:
        st.error("⚠️ This player is likely to **churn**.")
    else:
        st.success("✅ This player is likely to **stay loyal**.")

    st.markdown('</div>', unsafe_allow_html=True)

    # === Chart ===
    st.markdown('<div class="chart-panel">', unsafe_allow_html=True)
    fig, ax = plt.subplots(facecolor='none')
    labels = ['Churn', 'Loyal']
    colors = ['#ff6b6b', '#00bfa5']
    sizes = [100, 0] if result == 1 else [0, 100]
    ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'color': "#222", 'weight': 'bold'}
    )
    ax.axis('equal')
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

# === Footer ===
st.markdown('<div class="footer">⚙️ Powered by Artificial Intelligence | © 2025</div>', unsafe_allow_html=True)
