### ✅ **`README.md` for Insurance Dashboard SaaS**

---

# 📊 **Insurance Dashboard SaaS**

A **Streamlit-powered SaaS** platform for **insurance claim predictions**, developed using **React**, **Supabase**, **FastAPI**, and **Python (PyTorch & sklearn)**. This project predicts:
- **Claim occurrence** (whether a customer will claim or not).  
- **Claim amount** (the predicted amount of the claim).  

---

## 🚀 **Features**

### 🔥 **Core Functionalities**
- **CSV Upload**: Upload insurance-related CSV files via the Streamlit interface.  
- **ML Model Predictions**:
  - Model 1 → **Predicts claim occurrence** (`CLM_FLAG`: 0 or 1).  
  - Model 2 → **Predicts claim amount** (`CLM_AMT`).  
- **Database Integration**:  
  - Uses **Supabase** (PostgreSQL) to store and manage data.  
  - Each CSV upload creates a new table in Supabase.  
- **Real-Time Dashboard**:
  - Displays predictions with histograms, bar charts, and scatter plots.  
  - Visualizes key insights like **claim distribution** and **car usage patterns**.  

---

## ⚙️ **Tech Stack**

### ✅ **Frontend**
- **React** → Dynamic UI for user interaction.  
- **Streamlit** → Dashboard for displaying predictions and charts.  

### ✅ **Backend**
- **FastAPI** → Handles API requests, CSV uploads, and database interactions.  
- **Supabase** → PostgreSQL for cloud-hosted database management.  

### ✅ **Machine Learning**
- **PyTorch & sklearn** → Models trained on insurance data.  
- **Joblib** → Model serialization.  
- **LabelEncoders** → For categorical encoding of features.  

---

## 🛠️ **Installation & Setup**

### 🔥 **1. Clone the Repository**
```bash
git clone <repo_url>
cd insurance-dashboard
```

---

### 🛠️ **2. Set Up Backend**
- Install backend dependencies:
```bash
uv venv .venv
source .venv/bin/activate    # (Linux/macOS)
.venv\Scripts\activate        # (Windows)

uv pip install -r requirements.txt
```

- Create a `.env` file in `app/` directory:
```plaintext
SUPABASE_URL=<your_supabase_url>
SUPABASE_PASSWORD=<your_supabase_password>
```

- **Run FastAPI Server**
```bash
uvicorn app.main:app --reload
```

---

### 🔥 **3. Set Up Frontend**
- Install frontend dependencies:
```bash
npm install
```

- **Run Streamlit Dashboard**
```bash
streamlit run app/dashboard.py
```

---

## 📊 **Usage**

1. **Upload CSV** → Upload insurance CSV files via the Streamlit interface.  
2. **Prediction** → View predictions displayed in the dashboard with visualizations.  
3. **Data Storage** → CSV data and predictions are saved in Supabase.  

---

## 🔥 **Folder Structure**

```plaintext
📁 insurance-dashboard  
 ┣ 📁 app  
 ┃ ┣ 📄 main.py              # FastAPI backend server  
 ┃ ┣ 📄 load_db.py           # Supabase DB connection  
 ┃ ┣ 📄 ml_pipeline1.py      # Model 1 (claim occurrence)  
 ┃ ┣ 📄 ml_pipeline2.py      # Model 2 (claim amount)  
 ┃ ┣ 📄 dashboard.py         # Streamlit dashboard  
 ┃ ┣ 📄 requirements.txt     # Python dependencies  
 ┃ ┣ 📄 .env                 # Supabase credentials  
 ┃ ┗ 📁 models               # Trained models  
 ┣ 📁 frontend               # React Frontend  
 ┃ ┣ 📄 src/  
 ┃ ┣ 📄 public/  
 ┃ ┗ 📄 package.json  
 ┣ 📄 README.md  
 ┗ 📄 .gitignore  
```

---

## 📚 **API Endpoints**

### ✅ **Upload CSV & Predict Claim Amount**
```plaintext
POST /upload-csv-model2/
```
- **Description:** Uploads CSV and makes predictions for **claim amount** (`CLM_AMT`).  
- **Input:** CSV file  
- **Output:**  
```json
{
  "message": "CSV uploaded with predictions successfully!"
}
```

---

### ✅ **Fetch Model 2 Predictions**
```plaintext
GET /get-model2-data/
```
- **Description:** Fetches the latest predictions from Supabase.  
- **Output:**  
```json
{
  "data": [
    {
      "KIDSDRIV": 1,
      "AGE": 40.0,
      "INCOME": 28000.0,
      "CLM_AMT": 2657.69
    }
  ]
}
```

---

## 📊 **Visualization Examples**

### 💰 **Claim Amount Distribution**
- **Histogram** → Shows the frequency of different claim amounts.  
- **Bar Chart** → Displays the distribution of car usage.

---

## 🛠️ **Model Details**

### ✅ **Model 1: Claim Occurrence**
- **Algorithm:** Random Forest  
- **Input Features:**  
    - `AGE`, `INCOME`, `CAR_USE`, `CAR_TYPE`, etc.  
- **Output:**  
    - `CLM_FLAG` → 0 (no claim) or 1 (claim)  

---

### ✅ **Model 2: Claim Amount**
- **Algorithm:** Random Forest Regressor  
- **Input Features:**  
    - `AGE`, `INCOME`, `CAR_AGE`, `HOME_VAL`, etc.  
- **Output:**  
    - `CLM_AMT` → Predicted claim amount  

---

## 🚀 **Future Enhancements**
- Add **authentication** and user management.  
- Implement **CI/CD pipelines** for automated deployment.  
- Improve **model accuracy** with hyperparameter tuning.  
- Include **advanced charts** and analytics.  

---

## 🤝 **Contributing**
1. Fork the repository.  
2. Create a new branch:  
```bash
git checkout -b feature-name
```
3. Commit your changes:  
```bash
git commit -m "Add new feature"
```
4. Push to the branch:  
```bash
git push origin feature-name
```
5. Submit a pull request.  

---

## 📄 **License**
This project is licensed under the **MIT License**.

---

## 🚀 **Author**
- 👤 **Abhiram Adabala**  
- 📧 [Contact](mailto:your-email@example.com)  
- 🌐 [GitHub](https://github.com/AbhiramAdabala)  

---

✅ **Star this repo ⭐ if you find it helpful!** 🚀
