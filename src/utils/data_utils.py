import yfinance as yf
import os
import pandas as pd
from datetime import datetime


def select_stocks(config):
    stocks = config["project"]["stocks"]
    indices = config["project"]["indices"]
    start_date = config["project"]["train_period_start"]
    end_date = config["project"]["prediction_period_end"]
    return stocks, indices, start_date, end_date


def fetch_and_save_data(tickers, start, end, data_dir, label):
    """Veriyi Yahoo Finance API’den çekip csv olarak kaydeder."""
    for ticker in tickers:
        # Veri çekme
        data = yf.download(ticker, start=start, end=end)

        # Dosya ismi oluşturma
        file_name = f"{label}_{ticker}_{datetime.now().strftime('%Y%m%d')}.csv"
        file_path = os.path.join(data_dir, file_name)

        # Veriyi kaydetme
        data.to_csv(file_path)
        print(f"{ticker} verisi {file_path} olarak kaydedildi.")

