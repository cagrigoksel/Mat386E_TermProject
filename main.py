from src.etl.data_fetch import fetch_raw_data
from src.etl.load_to_postgres import load_raw_data_to_postgres
from src.etl.fetch_data_from_db import get_stock_data,get_index_data
import yfinance as yf
from src.utils.config_utils import load_config
def main():
    # 1. Fetch all the raw data that specified in the config.yaml and store it in the /data/raw/ folder.
    fetch_raw_data()

    # 2. Load all the raw data from /data/raw/ folder to PostgreSQL database.
    load_raw_data_to_postgres()

    # 3. Fetch the data from the PostgreSQL database.
    #get_stock_data() # Get the stock data from the PostgreSQL database.


if __name__ == "__main__":
    main()
