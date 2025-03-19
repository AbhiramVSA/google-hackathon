import joblib
import pandas as pd

# ✅ Load Encoders & Model
def load_encoders(file_path="C:/Users/abhir/Desktop/google-hackathon/app/label_encoders.pkl"):
    """Load saved LabelEncoders."""
    with open(file_path, "rb") as f:
        return joblib.load(f)

def load_model(file_path="C:/Users/abhir/Desktop/google-hackathon/app/random_forest_model.joblib"):
    """Load the trained model using joblib."""
    return joblib.load(file_path)

# ✅ Preprocess new data
def preprocess_new_data(new_df, label_encoders):
    """Preprocess new CSV data before passing to the ML model."""
    categorical_cols = ['model', 'fuel_type', 'engine_type', 'transmission_type', 
                        'steering_type', 'rear_brakes_type']

    # Apply saved LabelEncoders
    for col in categorical_cols:
        if col in new_df.columns and col in label_encoders:
            le = label_encoders[col]
            new_df[col] = new_df[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

    # Convert Yes/No to 1/0 for boolean columns
    bool_cols = ['is_esc', 'is_adjustable_steering', 'is_tpms', 'is_parking_sensors', 'is_parking_camera',
                 'is_front_fog_lights', 'is_rear_window_wiper', 'is_rear_window_washer',
                 'is_rear_window_defogger', 'is_brake_assist', 'is_power_door_locks',
                 'is_central_locking', 'is_power_steering', 'is_driver_seat_height_adjustable',
                 'is_day_night_rear_view_mirror', 'is_ecw', 'is_speed_alert']

    if all(col in new_df.columns for col in bool_cols):
        new_df[bool_cols] = new_df[bool_cols].replace({'Yes': 1, 'No': 0})

    # 🔥 Only apply `.str` on string columns
    if 'max_torque' in new_df.columns and new_df['max_torque'].dtype == 'object':
        new_df['max_torque'] = new_df['max_torque'].str.extract(r'(\d+\.?\d*)').astype(float)
    
    if 'max_power' in new_df.columns and new_df['max_power'].dtype == 'object':
        new_df['max_power'] = new_df['max_power'].str.extract(r'(\d+\.?\d*)').astype(float)

    return new_df


# ✅ Make predictions
def predict_new_data(new_df):
    """Make predictions and append to DataFrame."""
    label_encoders = load_encoders()
    model = load_model()

    # Preprocess new data
    processed_df = preprocess_new_data(new_df, label_encoders)

    # Ensure same columns as training data
    feature_columns = [col for col in processed_df.columns if col != 'claim_status']
    X_new = processed_df[feature_columns]

    # Make predictions
    predictions = model.predict(X_new)

    # Add predictions to the DataFrame
    new_df['claim_status'] = predictions

    return new_df
