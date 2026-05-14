import pandas as pd
import re
import nltk
import spacy

from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

# Download stopwords
nltk.download('stopwords')

from nltk.corpus import stopwords

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load cleaned dataset
df = pd.read_csv("data/raw/bank_reviews_cleaned.csv")

print("Dataset loaded successfully.")
print(df.head())

# -----------------------------------------
# TEXT CLEANING FUNCTION
# -----------------------------------------

stop_words = set(stopwords.words("english"))

def clean_text(text):

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # spaCy processing
    doc = nlp(text)

    tokens = []

    for token in doc:

        if token.text not in stop_words and not token.is_punct:
            tokens.append(token.lemma_)

    return " ".join(tokens)

# Apply cleaning
df["cleaned_review"] = df["review"].apply(clean_text)

print("Text cleaning completed.")

# -----------------------------------------
# SENTIMENT ANALYSIS
# -----------------------------------------

print("Loading transformer model...")

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

sentiments = []
scores = []

print("Running sentiment analysis...")

for text in df["review"]:

    try:

        result = classifier(text[:512])[0]

        label = result["label"]
        score = result["score"]

        # Convert to positive/negative/neutral
        if label == "POSITIVE":
            sentiment = "positive"
        elif label == "NEGATIVE" and score > 0.75:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        sentiments.append(sentiment)
        scores.append(score)

    except:
        sentiments.append("neutral")
        scores.append(0.50)

df["sentiment_label"] = sentiments
df["sentiment_score"] = scores

print("Sentiment analysis completed.")

# -----------------------------------------
# KEYWORD EXTRACTION
# -----------------------------------------

print("Extracting keywords using TF-IDF...")

vectorizer = TfidfVectorizer(
    max_features=100,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["cleaned_review"])

keywords = vectorizer.get_feature_names_out()

print("Top Keywords:")
print(keywords[:20])

# -----------------------------------------
# THEME IDENTIFICATION
# -----------------------------------------

def identify_theme(text):

    text = text.lower()

    if any(word in text for word in [
        "login", "password", "otp", "access"
    ]):
        return "Account Access Issues"

    elif any(word in text for word in [
        "transfer", "slow", "transaction", "loading"
    ]):
        return "Transaction Performance"

    elif any(word in text for word in [
        "ui", "design", "interface", "easy"
    ]):
        return "UI & User Experience"

    elif any(word in text for word in [
        "support", "service", "help"
    ]):
        return "Customer Support"

    elif any(word in text for word in [
        "fingerprint", "feature", "update", "option"
    ]):
        return "Feature Requests"

    else:
        return "Other"

df["identified_theme"] = df["cleaned_review"].apply(identify_theme)

print("Theme extraction completed.")

# -----------------------------------------
# FINAL OUTPUT
# -----------------------------------------

final_df = df[[
    "review",
    "rating",
    "date",
    "bank",
    "source",
    "sentiment_label",
    "sentiment_score",
    "identified_theme"
]]

final_df.to_csv(
    "data/raw/bank_reviews_analyzed.csv",
    index=False
)

print("Final analyzed dataset saved.")

# -----------------------------------------
# SUMMARY
# -----------------------------------------

print("\nSentiment Distribution:")
print(df["sentiment_label"].value_counts())

print("\nTheme Distribution:")
print(df["identified_theme"].value_counts())