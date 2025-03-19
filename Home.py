import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page config
st.set_page_config(page_title="ClaimSense", page_icon="🚗", layout="wide")

# Function to fetch a Lottie animation
def load_lottie_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception:
        return None

# Use a working Lottie animation URL
lottie_animation = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_ktwnwv5m.json")  

# Custom CSS for better styling
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .animated-title {
        font-size: 60px;
        font-weight: 800;
        text-align: left;
        color: #F3B61F;
        animation: fadeIn 1.5s ease-in-out;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
    }

    .subtext {
        font-size: 22px;
        text-align: left;
        color: #EDFFEC;
        font-weight: 600;
        animation: fadeIn 2s ease-in-out;
        margin-top: 5px;
    }

    .why-section {
        font-size: 20px;
        color: white;
        font-weight: 500;
        line-height: 1.8;
    }

    .button-container {
        text-align: left;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Two-column layout for proper alignment
col1, col2 = st.columns([1, 1.5])  # Adjusted column widths

with col1:
    if lottie_animation:
        st_lottie(lottie_animation, height=250, key="claim_animation")  # Reduced size
    else:
        st.warning("⚠ Animation failed to load. Check your internet connection or Lottie URL.")

with col2:
    st.markdown("<p class='animated-title'>Welcome to ClaimSense</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtext'>Revolutionizing automobile insurance with AI-driven claim predictions.</p>", unsafe_allow_html=True)

    st.markdown("<div class='why-section'>"
                "✅ AI-powered claim predictions.<br>"
                "✅ Faster and more accurate claim processing.<br>"
                "✅ Designed for B2B insurers to streamline operations.</div>", unsafe_allow_html=True)

    # Call to Action Button
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("🔍 Explore Dashboard"):
        st.switch_page("pages/1_Dashboard.py")
    st.markdown('</div>', unsafe_allow_html=True)
