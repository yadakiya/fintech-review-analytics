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
