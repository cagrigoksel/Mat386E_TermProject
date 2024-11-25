import psycopg2
import os
from src.utils.config_utils import load_config

def connect_db():
    """Veritabanına bağlanmak için ayarları yükler ve bağlantıyı oluşturur."""
    # Config dosyasını yükle

    config = load_config()
    
    db_config = config["database"]
    
    # Veritabanı bağlantısını oluştur
    conn = psycopg2.connect(
        host=db_config["host"],
        port=db_config["port"],
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"]
    )
    
    return conn