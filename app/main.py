from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from supabase import create_client, Client
import pandas as pd
import uuid
from app.load_db import Settings
from app.ml_pipeline1 import predict_new_data

settings = Settings()

app = FastAPI()

# ✅ Supabase Config
SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_KEY = settings.SUPABASE_PASSWORD
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ Supabase Table Name
TABLE_NAME = "vehicle_data_m1_op"

# ✅ Upload and process CSV
@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        # ✅ 1️⃣ Read CSV into DataFrame
        df = pd.read_csv(file.file)

        # ✅ 2️⃣ Make Predictions
        df_with_predictions = predict_new_data(df)

        # ✅ 3️⃣ Insert into Supabase
        data = df_with_predictions.to_dict(orient="records")
        insert_response = supabase.table(TABLE_NAME).insert(data).execute()

        # Check for errors in the response
        if hasattr(insert_response, 'error') and insert_response.error:
            raise Exception(f"Failed to upload to Supabase: {insert_response.error}")

        return JSONResponse(content={"message": "CSV uploaded with predictions successfully!"})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/get-model-data/")
async def get_model_data():
    """Fetch the latest predictions from Supabase."""
    try:
        response = supabase.table(TABLE_NAME).select("*").limit(50).execute()

        if hasattr(response, "data") and response.data:
            return JSONResponse(content={"data": response.data}, status_code=200)
        else:
            return JSONResponse(content={"message": "No data found"}, status_code=404)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)