import os

def setup_raw_dir():
    """Gerekli dizinleri oluşturur."""
    raw_data_dir = "data/raw"
    os.makedirs(raw_data_dir, exist_ok=True)
    return raw_data_dir