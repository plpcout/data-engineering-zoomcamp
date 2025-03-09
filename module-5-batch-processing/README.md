# Module 5 - Batch Processing

![Python](https://img.shields.io/badge/Python-3.12-4B8BBE.svg?style=flat&logo=python&logoColor=FFD43B&labelColor=306998)
[![SDKMan](https://img.shields.io/badge/SDKMan-1076C6?style=flat&logo=openjdk&logoColor=FFFFFF&labelColor=1076C6)](https://sdkman.io/)
![Apache Spark Badge](https://img.shields.io/badge/Apache%20Spark-E25A1C?logo=apachespark&logoColor=fff&style=flat)
[![PySpark](https://img.shields.io/badge/PySpark-3.5-262A38?style=flat-square&logo=apachespark&logoColor=E36B22&labelColor=262A38)](https://spark.apache.org/docs/latest/api/python/user_guide)
[![uv](https://img.shields.io/badge/astral/uv-261230?style=flat&logo=uv&logoColor=DE5FE9&labelColor=261230)](https://docs.astral.sh/uv/getting-started/installation/)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=E70488&labelColor=150458)](https://pandas.pydata.org/docs/user_guide/)

## Before starting

> [!IMPORTANT]
> This repo is part of my experimenting and studying the material of the Data Engineering Zoomcamp.
>
> For a more detailed explanation, or if you want to follow along the DataTalks.Club DE Zoomcamp, go check their official [data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) repository for its amazing content.

## Overview

This repository provides comprehensive resources and guides for **[Apache Spark](https://spark.apache.org/)**, focusing on many topics like **batch processing, data transformations, query optimization, cloud deployment** and more.

It covers **Spark SQL, DataFrames, cluster internals, group operations, and using Spark in cloud environments**. Also cloud solutions like **[Google Cloud Dataproc](https://cloud.google.com/dataproc?hl=en)**.

## Getting Started

### 🏁 To begin

1. Ensure you have **[Apache Spark](https://spark.apache.org/)** installed locally.
2. A **GCP** account with an active project.
3. **Optional**: Access to **Google Cloud Dataproc**.
4. Familiarity with **batch processing concepts** and **SQL** are recommended.
5. Follow the material starting from:
   - [📌 Introduction to Batch Processing and Apache Spark](./public_notes/5-1-notes.md).

> [!IMPORTANT]
>
> - Check the [Summary](#📖-summary), and **click** on the desired topic for a detailed note.
> - There's a [Navigation Menu](#navigation-menu) at the bottom for easy navigation.

## 📖 Summary

### 1. [Introduction to Batch Processing and Apache Spark](./public_notes/5-1-notes.md)

#### 🎯 1.1. Key Topics

- **Batch processing vs. Streaming**.
- **Apache Spark** as a distributed data processing engine.
- **Common batch processing workflows**.
- **When to use Spark vs. SQL-based processing**.
- **Typical Spark architecture and use cases**.

#### ⚡ 1.2. Highlights

- **Distributed computing** for handling large datasets efficiently.
- **Batch processing** for transforming data at scale.
- **Optimized for big data** workloads requiring flexible transformations.

---

### 2. [Installing Apache Spark](./public_notes/5-2-notes.md) (Optional)

#### 🎯 2.1. Key Topics

- **Installing Spark and dependencies**.
- **Setting up Spark with JDK and Hadoop**.
- **Configuring the environment for Spark development**.

#### ⚡ 2.2. Highlights

- **Easy setup** using SDKMan for Spark and Hadoop.
- **Virtual environment management** for dependencies.
- **Platform-independent installation guides**.

---

### 3. [Spark SQL and DataFrames](./public_notes/5-3-notes.md)

#### 🎯 3.1. Key Topics

- **Reading and writing data in Spark**.
- **Using DataFrames and defining schemas**.
- **Partitioning and query optimization**.
- **Built-in Spark functions and User-Defined Functions (UDFs)**.
- **Executing SQL queries within Spark**.

#### ⚡ 3.2. Highlights

- **SQL-like querying** on distributed datasets.
- **Optimized storage formats** such as Parquet.
- **Schema management** and transformations using PySpark.

---

### 4. [Spark Internals, GroupBy, and Joins](./public_notes/5-4-notes.md)

#### 🎯 4.1. Key Topics

- **Understanding Spark cluster components (Driver, Executors, Master Node)**.
- **How Spark manages distributed data partitions**.
- **Optimizing GroupBy and aggregation operations**.
- **Performing efficient Joins with Sort Merge and Broadcast strategies**.

#### ⚡ 4.2. Highlights

- **Optimized distributed computations** using partitioning.
- **Faster aggregations** with GroupBy optimizations.
- **Broadcast joins** for improving performance with small lookup tables.

---

### 5. [Running Spark in the Cloud](./public_notes/5-5-notes.md)

#### 🎯 5.1. Key Topics

- **Connecting Spark with Google Cloud Storage**.
- **Setting up and running a local Spark cluster**.
- **Deploying Spark jobs on Google Cloud Dataproc**.
- **Writing Spark output directly to BigQuery**.

#### ⚡ 5.2. Highlights

- **Cloud integration** with Google Cloud Storage and BigQuery.
- **Running Spark clusters on Dataproc** for scalable data processing.
- **Optimized data pipelines** using cloud-native services.

---

## Navigation Menu

| **Spark Topics**                                          | **Description**                                     |
|-----------------------------------------------------------|-----------------------------------------------------|
| [1. Introduction to Spark](./public_notes/5-1-notes.md)   | Overview of Spark and batch processing.             |
| [2. Installing Spark](./public_notes/5-2-notes.md)        | Setting up Spark and dependencies.                  |
| [3. Spark SQL & DataFrames](./public_notes/5-3-notes.md)  | Querying and transforming data with Spark SQL.      |
| [4. Spark Internals & Joins](./public_notes/5-4-notes.md) | Optimizing queries, GroupBy operations, and joins.  |
| [5. Running Spark in Cloud](./public_notes/5-5-notes.md)  | Deploying Spark workloads on Google Cloud.          |

---

[Back to the top](#module-5---batch-processing)
