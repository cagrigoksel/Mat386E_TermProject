import glob
import os
from utils.db_utils import get_spark_session, get_db_properties, get_db_url, load_csv_to_postgres

def load_raw_data_to_postgres():
    """Ham verileri PostgreSQL veritabanına yükler."""
    # Debug: Print current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Spark oturumunu başlatma
    spark = get_spark_session()

    try:
        # Veritabanı bağlantı ayarları
        db_url = get_db_url()
        db_properties = get_db_properties()

        # Use relative path from current working directory
        raw_data_dir = os.path.join(os.getcwd(), "data", "raw")
        print(f"Looking for CSV files in: {raw_data_dir}")
        
        # Check if directory exists
        if not os.path.exists(raw_data_dir):
            print(f"Directory not found: {raw_data_dir}")
            return

        # List all files in the directory
        print("Files in directory:")
        for file in os.listdir(raw_data_dir):
            print(f"  - {file}")

        # Find CSV files
        csv_files = glob.glob(os.path.join(raw_data_dir, "*.csv"))
        print(f"Found CSV files: {csv_files}")

        if not csv_files:
            print("No CSV files found!")
            return

        for file_path in csv_files:
            # Determine table name from filename
            if "stock" in file_path.lower():
                table_name = "stocks_data"
            elif "index" in file_path.lower():
                table_name = "indices_data"
            else:
                print(f"Skipping file {file_path} - unknown type")
                continue

            print(f"Loading {file_path} into {table_name}")
            # Load data
            load_csv_to_postgres(file_path, table_name, spark, db_url, db_properties)

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        spark.stop()

if __name__ == "__main__":
    load_raw_data_to_postgres()