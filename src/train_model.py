import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load processed dataset
df = pd.read_csv("data/processed_financial_data.csv")

mapping = {
    "Low":0,
    "Medium":1,
    "High":2
}

df["risk_encoded"] = df["risk_tolerance"].map(mapping)

features = [
"income",
"expenses",
"savings",
"debt",
"savings_rate",
"expense_ratio",
"debt_ratio"
]

X = df[features]
y = df["risk_encoded"]

X_train, X_test, y_train, y_test = train_test_split(
X,y,test_size=0.2,random_state=42
)

model = RandomForestClassifier(
n_estimators=200,
max_depth=6,
random_state=42
)

model.fit(X_train,y_train)

joblib.dump(model,"models/risk_model.pkl")

print("Model trained and saved.")