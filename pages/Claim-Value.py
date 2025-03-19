import streamlit as st
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ✅ FastAPI Backend URL
API_BASE_URL = "http://127.0.0.2:8001"

# ✅ Streamlit Page Config
st.set_page_config(page_title="📊 Insurance Model 2 Dashboard", page_icon="📈", layout="wide")
st.title("📊 Insurance Model 2 Dashboard")
st.subheader("Upload a CSV file to visualize predictions from Model 2.")

# ✅ Upload CSV
uploaded_file = st.file_uploader("Upload CSV for Model 2 (CLM_AMT Prediction)", type=["csv"])

if uploaded_file:
    st.write("### Uploading File...")

    # ✅ Upload CSV to FastAPI
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    response = requests.post(f"{API_BASE_URL}/upload-csv-model2/", files=files)

    if response.status_code == 200:
        st.success("File uploaded successfully!")

        # ✅ Fetch predictions from Supabase
        with st.spinner("Fetching predictions... Please wait."):
            time.sleep(3)

            # ✅ Fetch data from Supabase
            data_response = requests.get(f"{API_BASE_URL}/get-model2-data/")

            if data_response.status_code == 200:
                st.success("Predictions received!")

                # ✅ Convert response data to DataFrame
                df = pd.DataFrame(data_response.json()["data"])

                # ✅ Display the processed data
                st.write("### Processed Data Preview:")
                st.dataframe(df.head())

                # ✅ Binned Bar Chart for Claim Amount Distribution
                if "CLM_AMT" in df.columns:
                    st.write("### 💰 Claim Amount Distribution (Binned Bar Chart)")

                    # Bin the claim amounts into ranges
                    bin_edges = np.arange(0, df["CLM_AMT"].max() + 5000, 5000)  # Bins of 5000
                    labels = [f"{int(bin_edges[i])}-{int(bin_edges[i + 1])}" for i in range(len(bin_edges) - 1)]

                    df["CLM_AMT_Binned"] = pd.cut(df["CLM_AMT"], bins=bin_edges, labels=labels)

                    # Count occurrences in each range
                    amt_counts = df["CLM_AMT_Binned"].value_counts().sort_index()

                    # Plot bar chart
                    fig, ax = plt.subplots(figsize=(12, 6))
                    amt_counts.plot(kind="bar", color="skyblue", ax=ax)
                    ax.set_xlabel("Claim Amount Range")
                    ax.set_ylabel("Frequency")
                    ax.set_title("Binned Claim Amount Distribution")
                    plt.xticks(rotation=45)
                    st.pyplot(fig)

            else:
                st.error("Failed to fetch predictions.")
    else:
        st.error("File upload failed!")
