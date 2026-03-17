import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/processed_financial_data.csv")

features = df[["income","expenses","savings","debt"]]

scaler = StandardScaler()

scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3,random_state=42)

df["cluster"] = kmeans.fit_predict(scaled)

df.to_csv("data/final_financial_dataset.csv",index=False)

print("Clustering complete.")