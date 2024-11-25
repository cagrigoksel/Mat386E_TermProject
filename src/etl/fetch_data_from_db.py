import pandas as pd

from src.utils.config_utils import load_config
from src.utils.db_data_pull_utils import db_data_pull

def get_stock_data():
    config = load_config()
    symbols = config['project']['stocks']
    for symbol in symbols:
        return db_data_pull("stocks_data", symbol)

def get_index_data():
    config = load_config()
    symbols = config['project']['indices']
    for symbol in symbols:
        return db_data_pull("indices_data", symbol)