import glob
from src.utils.db_utils import get_spark_session, get_db_properties, get_db_url, load_csv_to_postgres

def load_raw_data_to_postgres():
    """Ham verileri PostgreSQL veritabanına yükler."""
    # Spark oturumunu başlatma
    spark = get_spark_session()

    try:
        # Veritabanı bağlantı ayarları
        db_url = get_db_url()
        db_properties = get_db_properties()

        # Ham veri klasöründeki CSV dosyalarını yükleme
        raw_data_dir = "data/raw/"
        csv_files = glob.glob(f"{raw_data_dir}/*.csv")

        for file_path in csv_files:
            # Dosya ismine göre tablo adını belirleme
            if "stock" in file_path:
                table_name = "stocks_data"
            elif "index" in file_path:
                table_name = "indices_data"

            # Veriyi yükleme
            load_csv_to_postgres(file_path, table_name, spark, db_url, db_properties)

    finally:
        spark.stop()

if __name__ == "__main__":
    load_raw_data_to_postgres()