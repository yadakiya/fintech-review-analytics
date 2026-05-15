import pandas as pd
from sqlalchemy import create_engine, text

# ---------------------------------------
# DATABASE CONNECTION
# ---------------------------------------

username = "postgres"
password = "postgres123"
host = "localhost"
port = "5433"
database = "bank_reviews"

engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)

print("Database connected successfully.")

# ---------------------------------------
# LOAD DATA
# ---------------------------------------

df = pd.read_csv("data/raw/bank_reviews_analyzed.csv")

print("Dataset loaded.")

# ---------------------------------------
# INSERT BANKS
# ---------------------------------------

banks = df["bank"].unique()
bank_mapping = {}

with engine.begin() as connection:

    for bank in banks:
        connection.execute(
            text("""
                INSERT INTO banks (bank_name, app_name)
                VALUES (:bank, :app)
                ON CONFLICT (bank_name) DO NOTHING;
            """),
            {"bank": bank, "app": f"{bank} Mobile Banking"}
        )

    print("Banks inserted.")

    # ---------------------------------------
    # FETCH BANK IDS
    # ---------------------------------------

    result = connection.execute(
        text("SELECT bank_id, bank_name FROM banks")
    )

    for row in result:
        bank_mapping[row.bank_name] = row.bank_id

    # ---------------------------------------
    # INSERT REVIEWS
    # ---------------------------------------

    for _, row in df.iterrows():

        connection.execute(
            text("""
                INSERT INTO reviews (
                    bank_id,
                    review_text,
                    rating,
                    review_date,
                    sentiment_label,
                    sentiment_score,
                    identified_theme,
                    source
                )
                VALUES (
                    :bank_id,
                    :review,
                    :rating,
                    :date,
                    :sentiment_label,
                    :sentiment_score,
                    :theme,
                    :source
                );
            """),
            {
                "bank_id": bank_mapping[row["bank"]],
                "review": row["review"],
                "rating": row["rating"],
                "date": row["date"],
                "sentiment_label": row["sentiment_label"],
                "sentiment_score": row["sentiment_score"],
                "theme": row["identified_theme"],
                "source": row["source"]
            }
        )

print("Reviews inserted successfully.")