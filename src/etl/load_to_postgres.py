from pyspark.sql import SparkSession
import psycopg2
import pandas as pd
import yaml
import glob
import os

# Config dosyasından ayarları yükleme
with open("../../config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Java 11'i kullan
os.environ['JAVA_HOME'] = '/Library/Java/JavaVirtualMachines/openjdk-11.jdk/Contents/Home'
os.environ['HADOOP_HOME_WARN_SUPPRESS'] = '1'

# Spark oturumunu başlatma
spark = SparkSession.builder \
    .appName("Stock_ETL") \
    .config("spark.driver.allowMultipleContexts", "true") \
    .config("spark.driver.extraJavaOptions", "-Djava.security.auth.login.config=/dev/null") \
    .config("spark.jars", "/Users/cagrigoksel/Downloads/postgresql-42.6.0.jar") \
    .master("local[*]") \
    .getOrCreate()

# Veritabanı bağlantı ayarları
db_config = config["database"]
db_url = f"jdbc:postgresql://{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
db_properties = {
    "user": db_config["user"],
    "password": db_config["password"],
    "driver": "org.postgresql.Driver"
}


# Veriyi PostgreSQL'e yükleme
def load_csv_to_postgres(csv_file_path, table_name):
    """CSV dosyasını PostgreSQL veritabanına yükler."""
    # CSV dosyasını Spark DataFrame olarak yükleme
    df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

    # PostgreSQL'e yükleme
    df.write.jdbc(url=db_url, table=table_name, mode="append", properties=db_properties)
    print(f"{csv_file_path} dosyası {table_name} tablosuna yüklendi.")


# Ham veri klasöründeki CSV dosyalarını yükleme
raw_data_dir = "../../data/raw/"
csv_files = glob.glob(f"{raw_data_dir}/*.csv")

for file_path in csv_files:
    # Dosya ismine göre tablo adını belirleme
    if "stock" in file_path:
        table_name = "stocks_data"
    elif "index" in file_path:
        table_name = "indices_data"

    # Veriyi yükleme
    load_csv_to_postgres(file_path, table_name)

spark.stop()
