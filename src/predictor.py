import joblib
import pandas as pd

model = joblib.load("models/risk_model.pkl")

def predict_risk(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    mapping = {
        0:"Low",
        1:"Medium",
        2:"High"
    }

    return mapping[prediction]