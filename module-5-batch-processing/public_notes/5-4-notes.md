# Spark Internals, GroupBy and Joins

## 📌 Overview

This section covers:

1. **Spark Internals** - The structure of a Spark cluster, including its components, execution process, and interactions with cloud storage systems.

2. **GroupBy operations** - How Spark implements GroupBy internally and optimizes performance allowing efficient aggregation of data across large datasets.

3. **Joins** - Spark provides different join strategies optimized for different data sizes and scenarios. This section covers the two main types of joins in Spark:

    - Joins between two large DataFrames.
    - Joins between a large DataFrame and a small DataFrame (**Broadcast Join**).

## 📖 Summary

1. [Internals Key Concepts](#🔑-internals-key-concepts)

   - The components of a **Spark Cluster** (Driver, Master, Executors).
   - The role of **Spark Submit** in job execution.
   - How Spark processes **distributed data partitions**.
   - The transition from **HDFS-based storage** to **cloud storage (S3, GCS, etc.)**.
   - The concept of **data locality** and its relevance in modern Spark environments.

2. [Group By Key Concepts](#🔑-group-by-key-concepts)

   - How Spark processes **GroupBy** operations.
   - The role of **executors, partitions, and reshuffling** in aggregation.
   - Optimization strategies to minimize **shuffle operations**.
   - How to **monitor GroupBy execution** in the Spark UI.

3. [Joins Key Concepts](#🔑-joins-key-concepts)

   - Different types of joins in Spark.
   - The **Sort Merge Join** strategy for large DataFrames.
   - The **Broadcast Join** strategy for optimizing joins with small tables.
   - The role of **reshuffling** and **external merge sort** in join execution.

## 🛠️ Prerequisites

- A working **PySpark** installation.
- Check [5-2-notes.md](../public_notes/5-2-notes.md)

## 📁 Files used in this section

- GroupBy and Joins notebook: [05_group_by_join.ipynb](../code/05_group_by_join.ipynb)

## 🔑 Internals Key Concepts

### Spark Cluster Components

A Spark cluster consists of multiple components working together to execute distributed computations efficiently.

#### Driver

- The **driver** is responsible for submitting jobs to the Spark cluster.
- It can be an **operator in Apache Airflow**, a **local script**, or any **orchestration tool**.

#### Spark Master

- The **Spark Master** acts as the **central coordinator** of the cluster.
- It receives jobs from the driver and assigns tasks to **executors**.
- Exposes a **web UI** (usually available at `http://localhost:4040`) to monitor execution.

#### Executors

- The **executors** are the worker nodes responsible for executing the assigned tasks.
- They fetch data from storage, perform computations, and write results back.
- If an executor fails, Spark **reassigns the work** to another available executor.

### Submitting Jobs to a Spark Cluster

A job is submitted to Spark using the `spark-submit` command:

```bash
spark-submit \
    --master spark://<master-url> \
    --deploy-mode cluster \
    my_spark_job.py
```

- `--master` specifies the Spark Master node.
- `--deploy-mode cluster` ensures execution on the cluster instead of locally.

### Distributed Data Processing in Spark

Spark divides datasets into **partitions**, allowing multiple executors to process data in parallel.

- Each **partition** is typically stored as a **Parquet file** in cloud storage.
- Executors pull these partitions and process them independently.
- Once computation is complete, results are stored back in the **data lake**.

#### Example: Parallel Data Processing

- Consider a dataset split into multiple **partitions**:

  ```bash
  Partition 1 -> Executor A
  Partition 2 -> Executor B
  Partition 3 -> Executor C
  ```

- If an executor completes its task, it moves to the **next available partition**, ensuring efficient resource utilization.

### The Evolution from HDFS to Cloud Storage

#### Traditional Hadoop-Based Storage

- In Hadoop-based architectures, data was stored in **HDFS (Hadoop Distributed File System)**.
- The concept of **data locality** was crucial—**executors processed data stored on their own disks** to reduce network overhead.
- Redundant copies of data were maintained across multiple nodes.

#### Transition to Cloud-Based Storage

- Modern Spark clusters store data in **cloud storage** (e.g., **AWS S3, Google Cloud Storage**).
- Cloud storage offers **scalability** and **cost efficiency**.
- Data locality is **less critical** because data transfer within the same cloud environment is fast.

### Summary of Spark Cluster Execution

1. The **driver** submits a job to the **Spark Master**.
2. The **master** distributes tasks across available **executors**.
3. **Executors** pull data partitions, perform computations, and store results.
4. If an executor fails, the master reassigns the workload.
5. Results are stored in **cloud storage** for further analysis.

## 🔑 Group By Key Concepts

### Understanding GroupBy in Spark

#### 1. Local Aggregation (Stage 1)

- Each **executor** processes a subset of data (partition).
- Grouping and aggregation occur **within each partition**.
- Intermediate results (sub-results) are stored.

#### 2. Global Aggregation (Stage 2)

- Spark **reshuffles** data so that records with the same key are grouped into the same partition.
- A second **aggregation step** combines sub-results.
- The final output is written to storage.

### Example: GroupBy in PySpark

#### Loading Data

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("GroupByExample").getOrCreate()

df = spark.read.option("header", "true").csv("data.csv")
```

#### Performing GroupBy

A few examples:

```python
grouped_df =df \
    .groupBy("name") \
    .agg({"age": "sum"}) \
    .sort("name") \
    .show()
```

```python
grouped_df = df \
    .groupBy(df.name) \
    .max() \
    .sort("name") \
    .show()
```

```python
grouped_df = df \
    .groupBy(["name", df.age]) \
    .count() \
    .sort("name", "age") \
    .show()
```

```python
grouped_df = df \
    .groupBy("zone", "hour") \
    .agg(
        sum("total_amount").alias("total_revenue"),
        count("trip_id").alias("trip_count")
    ) \
    .show()
```

### Optimization Strategies

#### 1. Repartitioning Data

- Change the number of partitions when needed.

```python
grouped_df = grouped_df.repartition(20)
```

#### 2. Avoiding Unnecessary Shuffle Operations

- Use **coalesce()** instead of **repartition()** when reducing partitions.

```python
grouped_df = grouped_df.coalesce(1)
```

#### 3. Monitoring Execution in Spark UI

- Track **shuffle operations** and **execution time** at `http://localhost:4040`.
- Identify expensive operations and **optimize partitioning**.

### GroupBy Execution Sequence

1. **Read and preprocess** data.
2. Perform **local aggregation** in each partition.
3. **Shuffle data** to group identical keys together.
4. Perform **global aggregation** and **write results** to storage.

## 🔑 Joins Key Concepts

### Joining Large DataFrames: Sort Merge Join

When both DataFrames are large, Spark performs a **Sort Merge Join**, which involves:

1. **Shuffling** the data to ensure all records with the same key are in the same partition.
2. **Sorting** each partition.
3. **Merging** matching records from both DataFrames.

#### Example

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkJoins").getOrCreate()

green_df = spark.read.parquet("data/revenue/green")
yellow_df = spark.read.parquet("data/revenue/yellow")

# Perform an Outer Join on 'hour' and 'zone' columns
df_join = green_df.join(yellow_df, on=["hour", "zone"], how="outer")
df_join.show()
```

**Execution Process:**

- Spark **reshuffles** data so that all matching keys are in the same partition.
- Uses **external merge sort** to efficiently join data.

### Optimizing Joins with Small Tables: Broadcast Join

When one table is much smaller than the other, Spark uses a **Broadcast Join**, which:

- **Broadcasts** the small table to all executors.
- **Performs an in-memory lookup** instead of a costly sort-merge operation.

#### Example

```python
zones_df = spark.read.parquet("data/zones")

df_result = df_join.join(zones_df, df_join.zone == zones_df.location_id, "left")
df_result = df_result.drop("location_id")
df_result.show()
```

**Execution Process:**

- The small DataFrame is **sent to all executors**.
- Executors **perform lookups locally**, avoiding expensive shuffling.

**Identifying Broadcast Joins in Execution Plans:**

- Spark UI will show **BroadcastExchange** instead of **Sort Merge Join**.
- **One-stage execution** instead of multiple shuffle stages.

## 📚 Additional Resources

- [Cluster Architecture](https://spark.apache.org/docs/latest/cluster-overview.html)
- [PySpark GroupBy](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.groupBy.html)
- [PySpark Join](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.join.html)
- [PySpark Join Types](https://sparkbyexamples.com/pyspark/pyspark-join-explained-with-examples/)
- [Spark UI](https://spark.apache.org/docs/latest/web-ui.html)

---

| [HOME](../README.md) | [<< BACK](./5-3-notes.md) | [NEXT >>](./5-5-notes.md) |
| -------------------- | ------------------------- | ------------------------- |
