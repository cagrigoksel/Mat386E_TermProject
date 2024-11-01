import yfinance as yf
import pandas as pd
import yaml
import os
from datetime import datetime

# Config dosyasından ayarları yükleme
with open("../../config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Hisse senetleri ve endeksler
stocks = ["AAPL", "NVDA", "MSFT"]  # Örnek olarak Apple, Nvidia ve Microsoft seçildi
indices = ["^GSPC", "^DJI"]  # Örnek olarak S&P 500 ve Dow Jones endeksleri

# Veri çekme parametreleri
start_date = config["project"]["train_period_start"]
end_date = config["project"]["prediction_period_end"]

# Veri kaydetme klasörü
raw_data_dir = "../../data/raw"
os.makedirs(raw_data_dir, exist_ok=True)


def fetch_and_save_data(tickers, start, end, data_dir, label):
    """Veriyi Yahoo Finance API’den çekip csv olarak kaydeder"""
    for ticker in tickers:
        # Veri çekme
        data = yf.download(ticker, start=start, end=end)

        # Dosya ismi oluşturma
        file_name = f"{label}_{ticker}_{datetime.now().strftime('%Y%m%d')}.csv"
        file_path = os.path.join(data_dir, file_name)

        # Veriyi kaydetme
        data.to_csv(file_path)
        print(f"{ticker} verisi {file_path} olarak kaydedildi.")


# Hisse senetleri ve endeks verilerini çekip kaydetme
fetch_and_save_data(stocks, start_date, end_date, raw_data_dir, "stock")
fetch_and_save_data(indices, start_date, end_date, raw_data_dir, "index")
