from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ServerExtraction").getOrCreate()

def fetch_from_server():
    file_path = "/path/to/server/patient_data.parquet"
    df = spark.read.parquet(file_path)
    
    # Write to S3
    df.write.parquet("s3a://your-s3-bucket-name/server_data.parquet")

fetch_from_server()
