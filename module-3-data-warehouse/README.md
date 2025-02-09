# Module 3 - Data Warehouse

[![](https://img.shields.io/badge/Google%20Cloud%20Platform-4285F4?style=flat&logo=googlecloud&logoColor=fff&labelColor=4285F4)](https://cloud.google.com/)
[![Google BigQuery Badge](https://img.shields.io/badge/Google%20BigQuery-669DF6?logo=googlebigquery&logoColor=fff&style=flat)](https://cloud.google.com/bigquery)
[![Docker](https://img.shields.io/badge/docker-2496ED?style=flat&logo=docker&logoColor=fff&labelColor=2496ED)](https://www.docker.com/)

## Before starting

> [!IMPORTANT]
> This repo is part of my experimenting and studying the material of the Data Engineering Zoomcamp.
>
> For a more detailed explanation, or if you want to follow along the DataTalks.Club DE Zoomcamp, go check their official [data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) repository for its amazing content.

## Overview

This repository covers essential topics and resources for **Google BigQuery**, focusing on **data warehousing, query optimization, best practices, and machine learning**.

## Getting Started

### 🏁 To begin

1. Ensure you have a **Google Cloud Platform (GCP) account** with **BigQuery access**.
2. Previous knowledge of **SQL** and basic data engineering concepts are recommended.

> [!IMPORTANT]
>
> - Check the [Summary](#📖-summary), and **click** on the desired topic for a detailed note.
> - There's a [Navigation Menu](#navigation-menu) at the bottom for easy navigation.

## 📖 Summary

### 1. [BigQuery Introduction](./public_notes/3-1-1-notes.md)

#### 🎯 1.1. Key Topics

- **OLTP vs OLAP**: Understanding transaction vs. analytical processing.
- **What is a Data Warehouse?**
- **BigQuery Features and Pricing Models**
- **Best Practices for Query Optimization**

#### ⚡ 1.2. Highlights

- **Cloud-native data warehouse** with serverless architecture.
- **Cost-efficient pricing models** for different workloads.
- **Separation of storage and compute** for better resource management.

---

### 2. [Partitioning and Clustering](./public_notes/3-1-2-notes.md)

#### 🎯 2.1. Key Topics

- **Partitioning:** Organizing large datasets efficiently.
- **Clustering:** Optimizing queries through intelligent column indexing.
- **Best practices for choosing between partitioning and clustering.**

#### ⚡ 2.2. Highlights

- **Improves query speed** by scanning only relevant data partitions.
- **Lowers storage costs** by optimizing data retrieval.
- **Enhances query performance** by reducing unnecessary scans.

---

### 3. [BigQuery Best Practices](./public_notes/3-2-1-notes.md)

#### 🎯 3.1. Key Topics

- **Optimizing queries for cost and performance.**
- **Using partitioned and clustered tables effectively.**
- **Avoiding unnecessary data scans to reduce costs.**

#### ⚡ 3.2. Highlights

- **Minimize query costs** by avoiding `SELECT *`.
- **Use partition filters** to reduce scanned data.
- **Optimize join operations** for better query execution.

---

### 4. [BigQuery Internals](./public_notes/3-2-2-notes.md)

#### 🎯 4.1. Key Topics

- **Colossus Storage**: How BigQuery manages data.
- **Jupiter Network**: High-speed interconnect for storage and compute.
- **Dremel Query Execution**: Parallel query processing for efficiency.

#### ⚡ 4.2. Highlights

- **Separation of storage & compute** for better scalability.
- **Parallel query execution** using Google's Dremel engine.
- **Columnar storage format** optimizes query speed and costs.

---

### 5. [BigQuery Machine Learning](./public_notes/3-3-1-notes.md)

#### 🎯 5.1. Key Topics

- **Introduction to BigQuery ML**: Running ML models inside BigQuery.
- **Building and training models with SQL.**
- **Evaluating model performance with BigQuery ML functions.**

#### ⚡ 5.2. Highlights

- **No external tools needed** for machine learning inside BigQuery.
- **Use SQL to train, evaluate, and predict** directly in BigQuery.
- **Supports multiple ML models** like linear regression and classification.

---

### 6. [Deploying BigQuery ML Models](./public_notes/3-3-2-notes.md)

#### 🎯 6.1. Key Topics

- **Exporting trained models from BigQuery ML.**
- **Setting up TensorFlow Serving for inference.**
- **Deploying models for real-time predictions.**

#### ⚡ 6.2. Highlights

- **Seamless model export from BigQuery to GCS.**
- **Run inference using Docker-based ML serving.**
- **Integrate ML models with API endpoints for real-time predictions.**

---

## Navigation Menu

| **BigQuery Topics**                                             | **Description**                                        |
| --------------------------------------------------------------- | ------------------------------------------------------ |
| [1. BigQuery Introduction](./public_notes/3-1-1-notes.md)       | Overview of BigQuery & Data Warehousing.               |
| [2. Partitioning and Clustering](./public_notes/3-1-2-notes.md) | Optimize query performance with partitions & clusters. |
| [3. BigQuery Best Practices](./public_notes/3-2-1-notes.md)     | Improve efficiency & reduce query costs.               |
| [4. BigQuery Internals](./public_notes/3-2-2-notes.md)          | Understand storage, networking, and execution.         |
| [5. BigQuery ML](./public_notes/3-3-1-notes.md)                 | Train ML models inside BigQuery using SQL.             |
| [6. Deploying ML Models](./public_notes/3-3-2-notes.md)         | Export, serve, and integrate ML models in production.  |

---

[Back to the top](#module-3---data-warehouse)
