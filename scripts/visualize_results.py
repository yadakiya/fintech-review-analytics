import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw/bank_reviews_analyzed.csv")

# -----------------------------------
# SENTIMENT DISTRIBUTION
# -----------------------------------

plt.figure(figsize=(10,6))

sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.savefig("data/raw/sentiment_distribution.png")

plt.close()

# -----------------------------------
# RATING DISTRIBUTION
# -----------------------------------

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="bank",
    y="rating"
)

plt.title("Rating Distribution by Bank")

plt.savefig("data/raw/rating_distribution.png")

plt.close()

# -----------------------------------
# THEME DISTRIBUTION
# -----------------------------------

theme_counts = (
    df["identified_theme"]
    .value_counts()
    .sort_values()
)

plt.figure(figsize=(10,6))

theme_counts.plot(kind="barh")

plt.title("Theme Frequency")

plt.xlabel("Count")

plt.savefig("data/raw/theme_frequency.png")

plt.close()

print("Visualizations generated successfully.")