# ==========================================================
# ETL Pipeline using PySpark
# Extract (CSV) -> Transform -> Load (Parquet)
# ==========================================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# ----------------------------------------------------------
# Step 1: Create Spark Session
# ----------------------------------------------------------
spark = SparkSession.builder \
    .appName("Sales ETL Pipeline") \
    .getOrCreate()

# ----------------------------------------------------------
# Step 2: Extract - Read CSV File
# ----------------------------------------------------------
df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

print("Original Data")
df.show()

print("Schema")
df.printSchema()

# ----------------------------------------------------------
# Step 3: Remove Duplicate Records
# ----------------------------------------------------------
df = df.dropDuplicates()

# ----------------------------------------------------------
# Step 4: Handle Missing Values
# ----------------------------------------------------------

# Fill missing Quantity with 1
df = df.fillna({"Quantity": 1})

# Remove rows where Customer is null
df = df.na.drop(subset=["Customer"])

print("Data after cleaning")
df.show()

# ----------------------------------------------------------
# Step 5: Create New Column (Total Sales)
# ----------------------------------------------------------
df = df.withColumn(
    "Total_Sales",
    col("Quantity") * col("Price")
)

print("Data with Total_Sales column")
df.show()

# ----------------------------------------------------------
# Step 6: Filter Products with Price > 1000
# ----------------------------------------------------------
filtered_df = df.filter(col("Price") > 1000)

print("Products with Price > 1000")
filtered_df.show()

# ----------------------------------------------------------
# Step 7: Sort by Total Sales (Descending)
# ----------------------------------------------------------
print("Sorted by Total Sales")
df.orderBy(col("Total_Sales").desc()).show()

# ----------------------------------------------------------
# Step 8: Aggregate Total Sales by Customer
# ----------------------------------------------------------
customer_sales = df.groupBy("Customer").agg(
    sum("Total_Sales").alias("Total_Sales")
)

print("Customer-wise Total Sales")
customer_sales.show()

# ----------------------------------------------------------
# Step 9: Load - Write to Parquet
# ----------------------------------------------------------
df.write.mode("overwrite").parquet("output/sales_parquet")

print("Parquet file written successfully!")

# ----------------------------------------------------------
# Step 10: Read Parquet (Verification)
# ----------------------------------------------------------
parquet_df = spark.read.parquet("output/sales_parquet")

print("Reading Parquet File")
parquet_df.show()

# ----------------------------------------------------------
# Stop Spark Session
# ----------------------------------------------------------
spark.stop()

print("ETL Pipeline Completed Successfully!")