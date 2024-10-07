import sys
import os

# Get the absolute path of the project root (one level up from 'src')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pandas as pd
from src.database.mongo_db import MongoDBClient
from src.logger.logger import get_logger

# Create a logger instance for this module
logger = get_logger(__name__)

class DataIngestion:
    def __init__(self):
        self.mongo_client = MongoDBClient(uri="mongodb://localhost:27017/", db_name="Synthetic_transaction")

    def load_csv_and_store(self, csv_file_path, collection_name):
        try:
            df = pd.read_csv(csv_file_path)
            logger.info(f"Data from {csv_file_path} loaded successfully!")
            records = df.to_dict(orient="records")
            self.mongo_client.insert_many_records(collection_name, records)
            logger.info(f"Data successfully stored in MongoDB collection '{collection_name}'")

        except Exception as e:
            logger.error(f"Error while loading data from CSV and storing in MongoDB: {e}")
            raise e  # Raise the exception if you want the script to stop

if __name__ == "__main__":
    csv_file_path = "C:/Users/sathy/OneDrive/Desktop/AML/AML/src/database/synthetic_transactions.csv"
    collection_name = "transactions"

    data_ingestion = DataIngestion()
    data_ingestion.load_csv_and_store(csv_file_path, collection_name)
