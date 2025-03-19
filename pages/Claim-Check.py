import streamlit as st
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

# ✅ FastAPI Backend URL
API_BASE_URL = "http://127.0.0.1:8000"  

# ✅ Streamlit Page Config
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
st.title("📊 ClaimSense Dashboard")
st.subheader("Upload a CSV file to visualize predictions from the model.")

# ✅ Upload CSV
uploaded_file = st.file_uploader("Upload CSV for Model (claim_status)", type=["csv"])

if uploaded_file:
    st.write("### Uploading File...")

    # ✅ Upload CSV to FastAPI
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    response = requests.post(f"{API_BASE_URL}/upload-csv/", files=files)

    if response.status_code == 200:
        st.success("File uploaded successfully!")

        # ✅ Fetch predictions from Supabase
        with st.spinner("Fetching predictions... Please wait."):
            time.sleep(3)

            # ✅ Fetch data from Supabase
            data_response = requests.get(f"{API_BASE_URL}/get-model-data/")

            if data_response.status_code == 200:
                st.success("Predictions received!")

                # ✅ Convert response data to DataFrame
                df = pd.DataFrame(data_response.json()["data"])

                # ✅ Display the processed data
                st.write("### Processed Data Preview:")
                st.dataframe(df.head())

                # ✅ Visualizations
                if "claim_status" in df.columns:
                    st.write("### 📊 Claim Status Distribution")
                    
                    # Bar chart for Claim Status Distribution
                    claim_counts = df["claim_status"].value_counts()
                    fig, ax = plt.subplots()
                    claim_counts.plot(kind="bar", ax=ax, color=["red", "green"])
                    ax.set_xlabel("Claim Status (0 = No Claim, 1 = Claimed)")
                    ax.set_ylabel("Number of Claims")
                    ax.set_title("Claim Status Distribution")
                    st.pyplot(fig)

                if "claim_amount" in df.columns:
                    st.write("### 💰 Claim Amount Distribution")
                    
                    # Histogram for Claim Amount Distribution
                    fig, ax = plt.subplots()
                    df["claim_amount"].hist(bins=20, ax=ax, color="skyblue", edgecolor="black")
                    ax.set_xlabel("Claim Amount")
                    ax.set_ylabel("Frequency")
                    ax.set_title("Claim Amount Distribution")
                    st.pyplot(fig)

            else:
                st.error("Failed to fetch predictions.")
    else:
        st.error("File upload failed!")
