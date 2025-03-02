# Introduction to Batch Processing

## 📌 Overview

Batch processing is a widely used method for processing large volumes of data in scheduled intervals. It allows for efficient data transformations, scalability, and integration with workflow orchestration tools. This section explores batch processing, its advantages, and common technologies used in its implementation.

## 📖 Summary

This section covers:

- The concept of batch processing and how it differs from streaming.
- Typical batch processing intervals such as daily, hourly, and weekly jobs.
- Common technologies used in batch processing, including Python, SQL, and Spark.
- The role of workflow orchestration tools like Airflow.
- Advantages and disadvantages of batch processing.

## 🛠️ Prerequisites

- The will to learn
- To get the most out of this; Minimal requirements:
  - Basic understanding of **SQL** and **Python**.
  - Familiarity with **data pipelines** and **workflow orchestration**.

## 🔑 Key Concepts

### Batch Processing vs. Streaming

- **Batch Processing**: Processes large chunks of accumulated data at scheduled intervals (e.g., daily or hourly jobs).
- **Streaming**: Processes data continuously in real-time as events occur.
- **Comparison**:
  - Batch jobs typically have a delay but are easier to manage.
  - Streaming allows immediate processing but requires more complex infrastructure.

### Common Batch Processing Intervals

- **Daily**: Most common, processes all collected data at the end of the day.
- **Hourly**: Processes accumulated data for each hour.
- **Weekly/Monthly**: Used for large-scale aggregations or reporting.
- **Less common**: Every few minutes or multiple times per hour.

### Technologies Used

- **Python scripts**: Often used for ingestion and transformation.
- **SQL**: Commonly used for transformations and aggregations.
- **Apache Spark**: A distributed processing engine for handling large datasets efficiently.
- **Other tools**: Frameworks like **Flink** or **Beam** can also be used for batch jobs.

### Workflow Orchestration

- **Airflow**: One of the most popular tool for scheduling and managing batch jobs.
- Other options include **Prefect**, **Mage**, **Kestra**, and various other workflow orchestration tools.
- **Example of a simple Workflow**:
  1. Ingest raw data from a **data lake** (CSV files, Parquet, etc.).
  2. Transform the data.
  3. Load processed data into a **data warehouse**.
  4. Trigger a **Spark job** for additional processing.

### Advantages of Batch Processing

- **Easy to manage**: Jobs run on fixed schedules and are retryable.
- **Scalable**: Can allocate more resources as needed.
- **Integration-friendly**: Works well with databases, cloud storage, and analytical tools.
- **80% ~ 90%** of jobs use batch processing over streaming.

### Disadvantages of Batch Processing

- **Latency**: Data is not immediately available.
- **Execution time**: Complex workflows can take significant time to complete.

## 🚀 Execution Flow

1. **Data is collected** over a predefined period (e.g., one day).
2. **Batch jobs process the data** using SQL, Python, or Spark.
3. **Processed data is stored** in a warehouse for analytics.
4. **Reports and dashboards** are generated based on batch-processed data.

## 📚 Additional Resources

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow](https://airflow.apache.org/)
