from scripts.Extract import extract_data
from scripts.Transform import clean_data
from scripts.Load import load_to_csv, load_to_postgres

RAW_FILE = "data/users-etl-data.csv"
PROCESSED_FILE = "cleaned/users_cleaned.csv"

def run_pipeline():
    for chunk in extract_data(RAW_FILE):
        cleaned_chunk = clean_data(chunk)

        # Load to CSV
        load_to_csv(cleaned_chunk, PROCESSED_FILE)

        # Load to PostgreSQL
        load_to_postgres(cleaned_chunk)

    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()