# Spark SQL and DataFrames

## 📌 Overview

This section explores the core functionalities of Spark, including working with DataFrames, executing SQL queries, optimizing query execution, and leveraging Spark’s distributed architecture for efficient computation.

📖 Summary

- Reading and writing data with PySpark
- Working with partitions
- Monitoring jobs using the Spark Master UI.
- Understanding Spark DataFrames and their schema.
- Using built-in functions for data manipulation.
- Defining and applying user-defined functions (UDFs)
- Querying data using **Spark SQL**.
- Registering DataFrames as SQL tables.

## 🛠️ Prerequisites

- A working **PySpark** installation.
- Check [5-2-notes.md](../public_notes/5-2-notes.md)

## 📁 Files used in this section

- PySpark Hands on notebook: [04_pyspark.ipynb](../code/04_pyspark.ipynb)
- PySpark SQL notebook: [06_spark_sql.ipynb](../code/06_spark_sql.ipynb)

> [!NOTE]
> Those are optional:
>
> [download_data.sh](../code/download_data.sh): downloads the taxi data raw files.
>
> [03_schemas.ipynb](../code/03_schemas.ipynb): transforms the raw data into parquet files.

## 🔑 Key Concepts

### Reading Data in PySpark

- Load `CSV` data with headers:

  ```python
  from pyspark.sql import SparkSession
  spark = SparkSession.builder.appName("FirstLook").getOrCreate()
  df = spark.read.option("header", "true").csv("file.csv")
  df.show(5)
  ```

- Spark does not infer csv data types automatically; all columns are initially treated as strings.

### Reading from pandas

- Use **Pandas** to load data into a dataframe:

  ```python
  # Spark can create a df from pandas df
  spark_df = spark.createDataFrame(df_pandas)
  ```

### Providing schema

  ```python
  from pyspark.sql import types

  # defining the schema to be used for the spark df -> argument in .schema()
  schema = types.StructType([
      types.StructField('hvfhs_license_num', types.StringType(), True),
      types.StructField('dispatching_base_num', types.StringType(), True),
      types.StructField('pickup_datetime', types.TimestampType(), True),
      types.StructField('dropoff_datetime', types.TimestampType(), True),
      types.StructField('PULocationID', types.IntegerType(), True),
      types.StructField('DOLocationID', types.IntegerType(), True),
      types.StructField('SR_Flag', types.StringType(), True)])
  ```

  eg.

  ```python
  # Spark can create a df from pandas df
  df = spark.read.option("header", "true").schema(schema).csv('file.csv')
  ```

### Understanding Partitions

- Spark distributes data into **partitions**, enabling parallel processing.
- Too few partitions cause idle executors, while too many cause overhead.
- Repartitioning data:

  ```python
  df = df.repartition(24)
  ```

- Partitions impact **performance**, especially when working with large datasets.

### Writing Data to Parquet

- Parquet is a compressed, columnar format optimized for analytics.
- Save data in **Parquet** format:

  ```python
  df.write.parquet("output_folder")
  ```

- If the output folder exists, Spark raises an error. To overwrite:

  ```python
  df.write.mode("overwrite").parquet("output_folder")
  ```

### Loading Data into a DataFrame

- Reading Parquet files (schema is automatically inferred):

  ```python
  df = spark.read.parquet("data.parquet")
  df.printSchema()  # Displays column names and data types
  ```

- Selecting specific columns:

  ```python
  df.select("pickup_datetime", "dropoff_datetime").show(5)
  ```

### Transformations and Actions

- **Transformations**: Operations that modify a DataFrame but are **lazy**, meaning they are not executed until an action is triggered.

  ```python
  df_filtered = df.filter(df.license_number == "12345")  # Transformation
  ```

- **Actions**: Operations that execute transformations and return results.

  ```python
  df_filtered.show(5)  # Action
  ```

- Other actions include:

  ```python
  df.count()  # Returns number of rows
  df.take(5)  # Returns first 5 rows as a list
  ```

### Using Built-in Functions

- Importing Spark SQL functions: (eg. `col` and `to_date`)

  ```python
  from pyspark.sql.functions import col, to_date
  ```

- Creating new columns:

  ```python
  df = df.withColumn("pickup_date", to_date(col("pickup_datetime")))
  ```

- Replacing existing columns:

  ```python
  df = df.withColumn("pickup_datetime", to_date(col("pickup_datetime")))
  ```

### User-Defined Functions (UDFs)

- Defining a custom function in Python:

  ```python
  def custom_function(base_number):
      return "my results"
  ```

- Converting it into a Spark UDF:

  ```python
  from pyspark.sql.functions import udf
  from pyspark.sql.types import StringType
  custom_function_udf = udf(custom_function, StringType())
  ```

- Applying the UDF:

  ```python
  df = df.withColumn("base_id", custom_function_udf(df.dispatching_base_number))
  ```

### Selecting Common Columns and Merging DataFrames

- Identify common columns across datasets:

  ```python
  common_columns = list(set(df_green.columns) & set(df_yellow.columns))
  ```

- Select common columns and add a `service_type` column:

- Combine the datasets using **union**:

  ```python
  df_trips = df_green_selected.union(df_yellow_selected)
  ```

### Registering a DataFrame as a SQL Table

- Convert a DataFrame into a temporary SQL table:

  ```python
  df_trips.createOrReplaceTempView("trips_data")
  ```

### Executing SQL Queries in Spark

- Query the registered table using SQL:

  ```python
  result_df = spark.sql(
      """
      SELECT service_type, COUNT(*) AS trip_count
      FROM trips_data
      GROUP BY service_type
      """
  )
  ```

- Show the results:

  ```python
  result_df.show()
  ```

### Writing Query Results to Parquet

- Save the query results in **Parquet format**:

  ```python
  result_df.write.parquet("data/reports/revenue", mode="overwrite")
  ```

- Reduce file fragmentation using **coalesce**:

  ```python
  result_df.coalesce(1).write.parquet("data/reports/revenue", mode="overwrite")
  ```

### Monitoring Spark Jobs

- The **Spark Master UI** runs on **port 4040**.
- View active and completed jobs at:

  ```bash
  http://localhost:4040
  ```

- Provides insights into **job execution**, **task distribution**, and **bottlenecks**.

## 📚 Additional Resources

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark Guide](https://spark.apache.org/docs/latest/api/python/)
- [Monitoring Spark Jobs](https://spark.apache.org/docs/latest/web-ui.html)
- [Spark SQL Functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html)
- [Parquet File Format](https://parquet.apache.org/)

---

| [HOME](../README.md) | [<< BACK](./5-2-notes.md) | [NEXT >>](./5-4-notes.md) |
| -------------------- | ------------------------- | ------------------------- |
