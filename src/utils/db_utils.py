import yaml
import os
from pyspark.sql.functions import lit, when, col, date_format, split, to_timestamp
from pyspark.sql import SparkSession
import tempfile
import atexit



def load_db_config(config_path="config.yaml"):
    """Veritabanı yapılandırma ayarlarını yükler."""
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config["database"]

def get_spark_session():
    """Spark oturumu başlatır ve döndürür."""
    from pyspark.sql import SparkSession
    import tempfile
    import atexit
    import os
    
    # Create a temporary directory that will be cleaned up on exit
    temp_dir = tempfile.mkdtemp()
    atexit.register(lambda: os.system(f'rmdir /S /Q "{temp_dir}"'))
    
    # Print the full path being used
    jdbc_path = r"C:\Users\deadp\postgresql-42.6.0.jar"
    print(f"Looking for JDBC driver at: {jdbc_path}")
    
    spark = SparkSession.builder \
        .appName("Stock_ETL") \
        .config("spark.driver.allowMultipleContexts", "true") \
        .config("spark.jars", jdbc_path) \
        .config("spark.worker.cleanup.enabled", "true") \
        .config("spark.storage.cleanupFilesAfterExecutor", "true") \
        .config("spark.sql.warehouse.dir", temp_dir) \
        .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2") \
        .config("spark.driver.extraJavaOptions", "-Dlog4j.logLevel=ERROR") \
        .config("spark.executor.extraJavaOptions", "-Dlog4j.logLevel=ERROR") \
        .master("local[*]") \
        .getOrCreate()
    
    # Set log level
    spark.sparkContext.setLogLevel("ERROR")
    
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
    """Load a CSV file into a PostgreSQL database."""
    try:
        # Load CSV as Spark DataFrame
        df = spark.read.csv(csv_file_path, header=True)

        # Extract symbol from filename
        if "stock_" in csv_file_path:
            symbol = os.path.basename(csv_file_path).split('_')[1]
        else:  # For index files
            symbol = os.path.basename(csv_file_path).split('_')[1].replace('^', '')

        # Filter out unwanted header rows
        df = df.filter(~col("Price").contains("Ticker"))

        # Convert columns and format the DataFrame
        df = df.select(
            to_timestamp(split(col("Price"), ",").getItem(0), "yyyy-MM-dd HH:mm:ss+00:00").alias("datetime"),
            split(col("Open"), ",").getItem(0).cast("float").alias("open"),
            split(col("High"), ",").getItem(0).cast("float").alias("high"),
            split(col("Low"), ",").getItem(0).cast("float").alias("low"),
            split(col("Close"), ",").getItem(0).cast("float").alias("close"),
            split(col("Adj Close"), ",").getItem(0).cast("float").alias("adj_close"),
            split(col("Volume"), ",").getItem(0).cast("float").alias("volume")
        )

        # Add symbol column
        df = df.withColumn("symbol", lit(symbol))

        # Delete existing data using psycopg2
        import psycopg2
        db_config = load_db_config()
        with psycopg2.connect(
            host=db_config['host'],
            database=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            port=db_config['port']
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM {table_name} WHERE symbol = %s", (symbol,))
            conn.commit()

        # Write new data to PostgreSQL
        df.write \
          .mode("append") \
          .jdbc(url=db_url, 
                table=table_name, 
                mode="append", 
                properties=db_properties)

        print(f"{csv_file_path} has been loaded into the {table_name} table.")

    except Exception as e:
        print(f"Error loading {csv_file_path}: {str(e)}")
        raise e


def test_db_connection():
    """Test database connection"""
    import psycopg2
    db_config = load_db_config()
    try:
        conn = psycopg2.connect(
            host=db_config['host'],
            database=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            port=db_config['port']
        )
        print("Database connection successful!")
        conn.close()
    except Exception as e:
        print(f"Error connecting to database: {e}")

def cleanup_spark_session(spark):
    """Clean up Spark session and resources."""
    if spark is not None:
        try:
            # Stop the Spark session
            spark.stop()
            
            # Force garbage collection
            import gc
            gc.collect()
            
        except Exception as e:
            print(f"Error during Spark cleanup: {str(e)}")

if __name__ == "__main__":
    test_db_connection()