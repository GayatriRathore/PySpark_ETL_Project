# PySpark ETL Pipeline (CSV → Transform → Parquet)

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built using PySpark.

The pipeline reads sales data from a CSV file, performs data cleaning and transformations, and stores the processed data in Parquet format for efficient analytics.

---

## Project Architecture

CSV File
      ↓
Read using PySpark
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
Write as Parquet
      ↓
Processed Data

---

## Technologies Used

- Python
- PySpark
- Apache Spark
- CSV
- Parquet
- VS Code

---

## Dataset

Input File:

data/sales.csv

Columns:

- Order_ID
- Customer
- Product
- Quantity
- Price

---

## Transformations Performed

- Read CSV file
- Removed duplicate records
- Handled missing values
- Removed rows with missing customer names
- Filled missing quantity with 1
- Created a new column: Total_Sales
- Filtered invalid records
- Sorted data by Total_Sales
- Aggregated total sales by customer
- Stored the cleaned data in Parquet format

---

## Project Structure

PySpark_ETL_Project/

├── data/
│   └── sales.csv

├── scripts/
│   └── etl_pipeline.py

├── output/
│   └── sales_parquet/

├── README.md

└── requirements.txt

---

## How to Run the Project

1. Clone the repository

git clone <repository-url>

2. Navigate to the project folder

cd PySpark_ETL_Project

3. Install dependencies

pip install pyspark

4. Run the ETL pipeline

python scripts/etl_pipeline.py

---

## Sample Output

The processed data includes a new column named **Total_Sales** and is saved in Parquet format inside the `output/sales_parquet/` folder.

Example:

| Order_ID | Customer | Product | Quantity | Price | Total_Sales |
|----------|----------|---------|----------|-------|-------------|
| 101 | Alice | Laptop | 2 | 60000 | 120000 |
| 102 | Bob | Mouse | 3 | 700 | 2100 |
| 103 | Charlie | Keyboard | 1 | 1500 | 1500 |

---

## Skills Demonstrated

- PySpark DataFrames
- ETL Pipeline Development
- Data Cleaning
- Handling Null Values
- Removing Duplicates
- Column Transformations
- Data Aggregation
- Writing Parquet Files
- Basic Data Engineering Concepts

---

## Future Enhancements

- Read data directly from Amazon S3
- Add logging
- Add exception handling
- Parameterize input and output paths
- Schedule the pipeline using Apache Airflow
- Load transformed data into a data warehouse

---

## Author

Gayatri Rathod