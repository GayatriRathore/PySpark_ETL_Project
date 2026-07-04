#To check if PySpark is installed correctly, you can run the following code in a Python environment:
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()

print("PySpark installed successfully!")
print(spark.version)

spark.stop()