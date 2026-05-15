# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian banking mobile applications:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The project includes:

- Google Play Store review scraping
- Data preprocessing
- Sentiment analysis
- Thematic analysis
- PostgreSQL database integration
- Data visualization
- Business recommendations

---

## Data Collection

Reviews were scraped using the `google-play-scraper` Python library.

Collected fields:

- Review text
- Rating
- Review date
- Bank name
- Source

---

## Preprocessing

The preprocessing pipeline includes:

- Missing value removal
- Duplicate removal
- Date normalization

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Transformers
- PostgreSQL
- Matplotlib
- Seaborn
## PostgreSQL Database

Database Name:
- bank_reviews

Tables:
- banks
- reviews

The database stores:
- review text
- ratings
- sentiment analysis
- themes
- source information

Python libraries used:
- SQLAlchemy
- psycopg2

## Sentiment Analysis

Sentiment analysis was performed using:
- DistilBERT transformer model
- Hugging Face transformers pipeline

Output labels:
- positive
- negative
- neutral

---

## Thematic Analysis

Themes were extracted using:
- TF-IDF keyword extraction
- Rule-based theme classification

Main themes:
- Account Access Issues
- Transaction Performance
- UI & User Experience
- Customer Support
- Feature Requests

---

## Visualizations

Generated plots include:
- sentiment distribution
- rating distribution
- theme frequency
- negative complaint analysis