from utils.data_utils import fetch_and_save_data
from utils.dir_utils import setup_dirs
from utils.data_utils import select_stocks
from utils.config_utils import load_config

def fetch_raw_data():
    """Tüm hisse senedi ve endeks verilerini çeker ve kaydeder."""
    # Config dosyasından ayarları yükleme
    config = load_config()

    # Hisse senetleri ve endeksler
    stocks, indices, start_date, end_date = select_stocks(config)

    # Veri kaydetme klasörü
    raw_data_dir = setup_dirs()

    # Veri çekme ve kaydetme
    fetch_and_save_data(stocks, start_date, end_date, raw_data_dir, "stock")
    fetch_and_save_data(indices, start_date, end_date, raw_data_dir, "index")

if __name__ == "__main__":
    fetch_raw_data()
