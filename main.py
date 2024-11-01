from src.etl.data_fetch import fetch_raw_data
from src.etl.load_to_postgres import load_raw_data_to_postgres

def main():
    # 1. Fetch all the raw data that specified in the config.yaml and store it in the /data/raw/ folder.
    fetch_raw_data()
    # 2. Load all the raw data from /data/raw/ folder to PostgreSQL database.
    load_raw_data_to_postgres()

if __name__ == "__main__":
    main()
