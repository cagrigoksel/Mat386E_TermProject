from src.utils.data_utils import fetch_and_save_data
from src.utils.dir_utils import setup_raw_dir
from src.utils.data_utils import select_stocks
from src.utils.config_utils import load_config

def fetch_raw_data():
    """Tüm hisse senedi ve endeks verilerini çeker ve kaydeder."""
    # Config dosyasından ayarları yükleme
    config = load_config()

    # Hisse senetleri ve endeksler
    stocks, indices, start_date, end_date = select_stocks(config)

    # Veri kaydetme klasörü
    raw_data_dir = setup_raw_dir()

    # Veri çekme ve kaydetme
    fetch_and_save_data(stocks, start_date, end_date, raw_data_dir, "stock")
    fetch_and_save_data(indices, start_date, end_date, raw_data_dir, "index")

if __name__ == "__main__":
    fetch_raw_data()
