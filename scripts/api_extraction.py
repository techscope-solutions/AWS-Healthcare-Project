from pyspark.sql import SparkSession
import requests

spark = SparkSession.builder.appName("APIExtraction").getOrCreate()

def fetch_from_api():
    # Sample API Endpoint
    response = requests.get("https://api.example.com/patient-data")

    if response.status_code == 200:
        data = response.json()
        df = spark.read.json(data)
        
        # Write to S3
        df.write.parquet("s3a://your-s3-bucket-name/api_data.parquet")

fetch_from_api()
