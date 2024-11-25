import yaml
from pyspark.sql import SparkSession
from src.utils.config_utils import load_config
import os


def load_db_config(config_path="config.yaml"):
    """Veritabanı yapılandırma ayarlarını yükler."""
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config["database"]

def get_spark_session():
    """Spark oturumu oluşturur ve yapılandırır."""
    # Java ayarları
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
    
    return spark

def get_db_properties():
    """PostgreSQL bağlantı özelliklerini döndürür."""
    db_config = load_db_config()
    return {
        "user": db_config["user"],
        "password": db_config["password"],
        "driver": "org.postgresql.Driver"
    }

def get_db_url():
    """PostgreSQL JDBC URL'sini oluşturur."""
    db_config = load_db_config()
    return f"jdbc:postgresql://{db_config['host']}:{db_config['port']}/{db_config['dbname']}"


def load_csv_to_postgres(csv_file_path, table_name, spark, db_url, db_properties):
    """CSV dosyasını PostgreSQL veritabanına yükler."""
    # CSV dosyasını Spark DataFrame olarak yükleme
    df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

    # PostgreSQL'e yükleme
    df.write.jdbc(url=db_url, table=table_name, mode="append", properties=db_properties)
    print(f"{csv_file_path} dosyası {table_name} tablosuna yüklendi.")