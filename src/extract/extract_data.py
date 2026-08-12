import logging
import os
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

def extract_data(file_path):
    logger.info(f"Starting extraction from: {file_path}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    logger.info(f"Input file found")

    df = pd.read_csv(file_path)

    logger.info(f"CSV file successfully read")

    if df.empty:
        raise ValueError("File does not contain any data")

    required_columns = {
    "patient_id",
    "first_name",
    "last_name",
    "date_of_birth",
    "gender",
    "city"
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    logger.info(f"Records loaded: {len(df)}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 records:")
    print(df.head())

    return df


file_path = "data/raw/patients_day1.csv"

df = extract_data(file_path)
