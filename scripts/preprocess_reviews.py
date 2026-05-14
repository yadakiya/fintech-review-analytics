import pandas as pd

df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Initial Shape:", df.shape)

# Remove missing values
df = df.dropna(subset=["review", "rating"])

# Remove duplicates
df = df.drop_duplicates(subset=["review"])

# Normalize date
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

print("Cleaned Shape:", df.shape)

df.to_csv("data/raw/bank_reviews_cleaned.csv", index=False)

print("Cleaned dataset saved.")