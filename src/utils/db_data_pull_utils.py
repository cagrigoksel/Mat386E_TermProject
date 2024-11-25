import pandas as pd

from src.utils.db_connect_utils import connect_db
from src.utils.config_utils import load_config

def db_data_pull(table_name, Ticker=None):
    """Verilen tablo adından belirli bir stok veya endeks verisini çekmek için fonksiyon."""

    config = load_config()
    
    start_date = config['project']['train_period_start']
    end_date = config['project']['prediction_period_end']

    conn = connect_db()  # Veritabanı bağlantısını oluştur

    # Temel sorgu
    query = f"SELECT * FROM {table_name} WHERE 1=1"  # 1=1, dinamik olarak filtre eklemek için başlangıç

    # Filtreleri ekle
    if Ticker:
        query += f" AND Ticker = '{Ticker}'"  # Sembol filtresi
    if start_date:
        query += f" AND date >= '{start_date}'"  # Başlangıç tarihi filtresi
    if end_date:
        query += f" AND date <= '{end_date}'"  # Bitiş tarihi filtresi

    try:
        # Sorguyu çalıştır ve DataFrame'e dönüştür
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"Veri çekme sırasında bir hata oluştu: {str(e)}")
        return None
    finally:
        conn.close()  # Bağlantının kapatıldığından emin ol