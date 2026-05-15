import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------
# LOAD DATA
# ------------------------------------

df = pd.read_csv(
    "data/raw/bank_reviews_analyzed.csv"
)

print("Dataset loaded successfully.")

# ------------------------------------
# AVERAGE RATING PER BANK
# ------------------------------------

avg_rating = (
    df.groupby("bank")["rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Ratings:")
print(avg_rating)

# ------------------------------------
# SENTIMENT DISTRIBUTION
# ------------------------------------

sentiment_counts = (
    df.groupby(["bank", "sentiment_label"])
    .size()
    .reset_index(name="count")
)

plt.figure(figsize=(10,6))

sns.barplot(
    data=sentiment_counts,
    x="bank",
    y="count",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Review Count")

plt.savefig("data/raw/final_sentiment_distribution.png")

plt.close()

# ------------------------------------
# THEME FREQUENCY
# ------------------------------------

theme_counts = (
    df.groupby(["bank", "identified_theme"])
    .size()
    .reset_index(name="count")
)

plt.figure(figsize=(12,6))

sns.barplot(
    data=theme_counts,
    x="identified_theme",
    y="count",
    hue="bank"
)

plt.xticks(rotation=20)

plt.title("Theme Frequency by Bank")

plt.savefig("data/raw/final_theme_analysis.png")

plt.close()

# ------------------------------------
# RATING DISTRIBUTION
# ------------------------------------

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="bank",
    y="rating"
)

plt.title("Rating Distribution by Bank")

plt.savefig("data/raw/final_rating_distribution.png")

plt.close()

# ------------------------------------
# TOP NEGATIVE THEMES
# ------------------------------------

negative_reviews = df[
    df["sentiment_label"] == "negative"
]

negative_theme_counts = (
    negative_reviews["identified_theme"]
    .value_counts()
)

plt.figure(figsize=(10,6))

negative_theme_counts.plot(kind="bar")

plt.title("Most Common Negative Themes")

plt.ylabel("Count")

plt.savefig("data/raw/final_negative_themes.png")

plt.close()

print("All final visualizations generated.")