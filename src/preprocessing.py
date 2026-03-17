import pandas as pd

# Load dataset
df = pd.read_csv("data/financial_data.csv")

# Feature engineering
df["savings_rate"] = df["savings"] / df["income"]
df["expense_ratio"] = df["expenses"] / df["income"]
df["debt_ratio"] = df["debt"] / df["income"]

# Handle missing values
df = df.fillna(0)

# Save processed dataset
df.to_csv("data/processed_financial_data.csv", index=False)

print("Processed dataset saved.")