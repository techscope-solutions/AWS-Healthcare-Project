from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DBExtraction").getOrCreate()

def fetch_from_db():
    db_properties = {
        "user": "your_db_user",
        "password": "your_db_password",
        "driver": "org.postgresql.Driver"
    }

    db_url = "jdbc:postgresql://your_db_host:your_db_port/your_dbname"

    df = spark.read.jdbc(db_url, "patient_table", properties=db_properties)
    
    # Write to S3
    df.write.parquet("s3a://your-s3-bucket-name/db_data.parquet")

fetch_from_db()
