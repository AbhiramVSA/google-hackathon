import joblib
import pandas as pd

# ✅ Load Encoders & Model
def load_encoders(file_path="C:/Users/abhir/Desktop/google-hackathon/app/label_encoders_model2.pkl"):
    """Load saved LabelEncoders."""
    with open(file_path, "rb") as f:
        return joblib.load(f)

def load_model(file_path="C:/Users/abhir/Desktop/google-hackathon/app/random_forest_model2.joblib"):
    """Load the trained model using joblib."""
    return joblib.load(file_path)

# ✅ Preprocess new data
def preprocess_new_data(new_df, label_encoders):
    """Preprocess new CSV data before passing to the ML model."""
    categorical_cols = ['GENDER', 'EDUCATION', 'OCCUPATION', 'CAR_USE', 'CAR_TYPE', 'PARENT1', 'MSTATUS', 'URBANICITY']

    # Apply saved LabelEncoders
    for col in categorical_cols:
        if col in new_df.columns and col in label_encoders:
            le = label_encoders[col]
            new_df[col] = new_df[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

    return new_df

# ✅ Make predictions
def predict_new_data(new_df):
    """Make predictions and append to DataFrame."""
    label_encoders = load_encoders()
    model = load_model()

    # Preprocess new data
    processed_df = preprocess_new_data(new_df, label_encoders)

    # Ensure same columns as training data
    feature_columns = [col for col in processed_df.columns if col != 'CLM_AMT']
    X_new = processed_df[feature_columns]

    # Make predictions
    predictions = model.predict(X_new)

    return predictions
