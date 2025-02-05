# ETL Pipelines with Kestra on Google Cloud Platform

## 📌 Overview

An **ETL (Extract, Transform, Load) pipeline** is essential for managing and analyzing large datasets.
This note covers how to set up and run an ETL pipeline using **Kestra**, as an orchestration tool that simplifies workflow automation, and **Google Cloud Platform (GCP)** as the cloud platform of choice.

- Extract CSV data and store it in **Google Cloud Storage (GCS)**
- Load data into **BigQuery** for processing
- Automate the pipeline with **Kestra workflows**


## ⚙️ Prerequisites

Before setting up the ETL pipeline, ensure you have the following:

- **Google Cloud Platform (GCP) Account** – [Sign up here](https://cloud.google.com/)
- **GCP Project** with Billing enabled
- **Google Cloud SDK** installed – [Installation Guide](https://cloud.google.com/sdk/docs/install)
- **Service Account with necessary permissions**:
  - `Storage Admin` 📁 (to manage GCS)
  - `BigQuery Admin` 📊 (to manage BigQuery)

## 📁 Files used in this notebook
- Kestra **`gcp_kv`** flow [2-2-6-1-flow.yml](../flows/2-2-6-1-flow.yml)
- Kestra **`gcp_setup`** flow [2-2-6-2-flow.yml](../flows/2-2-6-2-flow.yml)
- Kestra **`gcp_taxi`** flow [2-2-6-3-flow.yml](../flows/2-2-6-3-flow.yml)

## 🏗️ Key Concepts

### 🔹 Google Cloud Storage (GCS)
- **What is it?** A scalable object storage system for structured and unstructured data.
- **Use case:** Stores CSV files before processing in BigQuery.
- **Benefits:** Secure, cost-effective, and optimized for cloud storage.

### 🔹 BigQuery
- **What is it?** A fully managed, serverless data warehouse for large-scale data analytics.
- **Use case:** Processes structured data with SQL-based queries.
- **Benefits:** Fast, scalable, and integrates with various data sources.

## ☁️ Setting Up Google Cloud
1. **Create a GCP Project** → [Google Cloud Console](https://console.cloud.google.com/) 🌍
2. **Enable Services:** BigQuery, Cloud Storage.
3. **Create a Service Account** with permissions:
   - `Storage Admin` 📁 (to manage GCS)
   - `BigQuery Admin` 📊 (to manage BigQuery)
4. **Generate a JSON Key** 🔑 and store it securely.

## ⚙️ Configuring Kestra
- **Use Key-Value Store** for managing project configurations and secrets.

    ```yml
    tasks:
    - id: gcp_project_id
        type: io.kestra.plugin.core.kv.Set
        key: GCP_PROJECT_ID
        kvType: STRING
        value:  your-project-id
    ```

    - Check **`gcp_kv`** flow [2-2-6-1-flow.yml](../flows/2-2-6-1-flow.yml) for more details.

- **Set Up Plugin Defaults** to simplify authentication and configuration.
  ```yml
  pluginDefaults:
    - type: io.kestra.plugin.gcp
      values:
        projectId: "{{kv('GCP_PROJECT_ID')}}"
        location: "{{kv('GCP_LOCATION')}}"
        bucket: "{{kv('GCP_BUCKET_NAME')}}"
  ```

> [!IMPORTANT]
>
> **GCP** service account - The file should be bound into the Kestra container and exposed inside the container for proper access.
>
>For more details, refer to the [google credentials documentation](https://kestra.io/docs/how-to-guides/google-credentials).


## 📤 Uploading Data to GCS
1. **Run the [Setup Workflow](#) to create:**
   - **GCS Bucket**
   - **BigQuery Dataset**

     - Check **`gcp_setup`** flow [2-2-6-2-flow.yml](../flows/2-2-6-2-flow.yml) for more details.


2. **Now into the `main_flow`**:
    - Run the Extract **CSV Files** from [NYC Taxi Data](https://github.com/DataTalksClub/nyc-tlc-data/releases)
    - Task `id: extract`
      - Check **`gcp_taxi`** flow [2-2-6-3-flow.yml](../flows/2-2-6-3-flow.yml) for more details.

## 🔄 ETL Pipeline Tasks

> [!NOTE]
>
> Check the [main_flow.yml](#)

### 🗂️ **Extract**
- Download raw data (e.g., [NYC Taxi Data](https://github.com/DataTalksClub/nyc-tlc-data/releases)).
- Prepare the dataset for further processing.

---

### ☁️ **Upload to GCS**
- Upload the raw CSV file to **Google Cloud Storage (GCS)**.
- Store the data in a cloud repository for accessibility and scalability.

---

### ⚙️ **Conditional Task: (Green/Yellow)**
- **Evaluate dataset type**: Determine if the data is “green” or “yellow.”
- **Route processing**: Execute different processing paths based on data type.

---

### 🏗️ **Create BigQuery Table**
- **Check table existence**: Create a new structured table in **BigQuery** if it doesn’t exist.
- **Store structured data**: Set up the table to hold the further processed data.

---

### 🛠️ **Create External Table**
- **Define external table**: Link BigQuery to the raw data stored in GCS.
- **Access raw data** directly from the cloud storage without moving it into BigQuery.

---

### 📝 **Create Temporary Table**
- **Load data into temporary table**: Transfer data from the external table to a temporary staging table in BigQuery.
- **Apply transformations**: Add necessary transformations (e.g., `unique_row_id`) during the staging process.

---

### 🔄 **Merge Data**
- **Merge new records** from the temporary table into the main BigQuery table.
- **Avoid duplicates**: Ensure data consistency and integrity.

---

### 🧹 **Cleanup Temporary Tables (Optional)**
- **Delete/Move temporary tables**: Remove or archive temporary staging tables to save space.
- **Prevent clutter**: Free up resources for the next cycle of processing.

---

### 🗑️ **Purge Temporary Files**
- **Remove processed files** from the application storage.
- **Maintain efficiency** by clearing unnecessary files and optimizing storage.

---

## ✅ Key Takeaways
✔️ **Cloud-based ETL** enables scalable data processing.

✔️ **Kestra workflows** simplify complex orchestration.

✔️ **BigQuery** provides powerful analytics with SQL.

✔️ **GCS as a data lake** ensures efficient data storage.

---

| [HOME](../README.md) | [<< BACK](./2-2-5-notes.md) | [NEXT >>](./2-2-7-notes.md) |
| -------------------- | ----------------------- | --------------------------- |
