import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1200

data = {
    "age": np.random.randint(22, 60, rows),
    "income": np.random.randint(30000, 150000, rows),
    "expenses": np.random.randint(15000, 90000, rows),
    "savings": np.random.randint(5000, 80000, rows),
    "debt": np.random.randint(0, 50000, rows)
}

df = pd.DataFrame(data)

conditions = [
    (df["savings"] > 40000),
    (df["savings"] <= 40000) & (df["savings"] > 15000),
    (df["savings"] <= 15000)
]

choices = ["Low", "Medium", "High"]

# FIX: add default value
df["risk_tolerance"] = np.select(conditions, choices, default="Medium")

df.to_csv("data/financial_data.csv", index=False)

print("Dataset generated successfully!")