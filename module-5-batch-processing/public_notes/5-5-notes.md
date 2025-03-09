# Running Spark in the Cloud

## 📌 Overview

This section covers:

1. **Connecting to Google Cloud Storage** - Set up Spark to connect with GCS, configuring authentication, and performing basic operations on cloud-stored data.

2. **Creating a Local Spark Cluster** - Set up a local Spark cluster, convert a Jupyter Notebook into a Python script, and use `spark-submit` to execute Spark jobs efficiently.

3. **Setting up a Dataproc Cluster** - Set up a Dataproc cluster. Google Cloud Dataproc is a managed service that simplifies running Apache Spark and other big data applications on Google Cloud Platform.

4. **Connecting Spark to Big Query** - Set up Dataproc to write data directly to BigQuery without needing to store intermediate results in Google Cloud Storage.

## 📖 Summary

1. [GCS Connect Key Concepts](#🔑-gcs-connect-key-concepts)

   - Installing and configuring the **GCS connector for Spark**.
   - Creating a Spark session with the necessary configurations.
   - Running a test query to verify the connection.

2. [Local Cluster Key Concepts](#🔑-local-cluster-key-concepts)

   - Create a standalone Spark cluster with a master and worker nodes.
   - Use `spark-submit` to submit Spark jobs.
   - Ensure proper cleanup of Spark processes after execution.

3. [Dataproc Cluster Key Concepts](#🔑-dataproc-cluster-key-concepts)

    - Create a Dataproc cluster on Google Cloud
    - Submit a Spark job via the web UI
    - Submit a job using Google Cloud SDK

4. [Dataproc to BQ Key Concepts](#🔑-dataproc-to-bq-key-concepts)

    - Modify the Spark Job to Write to BigQuery
    - Upload the Script to Google Cloud Storage
    - Submit the Job Using Google Cloud SDK

## 🛠️ Prerequisites

- A Google Cloud Platform (GCP) account
- A working **Apache Spark** installation.
- **Google Cloud SDK** installed (`gcloud` CLI).

## 🔑 GCS Connect Key Concepts

### Uploading Data to Google Cloud Storage

- Copy files to GCS using `gsutil`:

   ```bash
   gsutil -m cp -r pq gs://your-bucket-name/pq/
   ```

  - `-m`: Enables multi-threading for faster uploads.
  - `-r`: Copies directories recursively.

### Installing the GCS Connector for Spark

1. Create a directory for storing the JAR file:

   ```bash
   mkdir libs
   ```

2. Download the latest GCS connector JAR:

   ```bash
   gsutil cp gs://hadoop-lib/gcs/gcs-connector-hadoop3-2.2.5.jar libs/
   ```

### Configuring Spark to Use Google Cloud Storage

To enable Spark to interact with GCS, specific configurations must be added when initializing Spark.

- Check the implementation on Spark GCS notebook: [07_spark_gcs.ipynb](../code/07_spark_gcs.ipynb)

### Reading Data from GCS

```python
df = spark.read.parquet("gs://your-bucket-name/pq/data.parquet")
df.show(5)
```

If the operation succeeds without errors, the integration is set up correctly.

## 🔑 Local Cluster Key Concepts

### 1. Starting a Spark Master

Run the following command in the terminal to start a Spark master process:

```sh
cd $SPARK_HOME
sbin/start-master.sh
```

Once started, the Spark Master UI can be accessed at `http://localhost:8080`.

### 2. Starting a Spark Worker

After launching the master, start a worker node:

```sh
sbin/start-slave.sh spark://your-master-url:port
```

Verify the worker appears in the Spark Master UI.

### 3. Using `spark-submit`

Instead of executing the script ([04_spark_sql.py](../code/04_spark_sql.py)) directly, use `spark-submit` to run it with more control:

```sh
MASTER_URL="spark://your-master-url:port"
spark-submit \
    --master ${MASTER_URL} \
    04_spark_sql.py \
        --input_green data/pq/green/2021/* \
        --input_yellow data/pq/yellow/2021/* \
        --output data/report/2021
```

This approach allows specifying the master, resource allocation, and input/output locations dynamically.

### 4. Stopping Spark Processes

Once done, stop the Spark cluster to free resources:

```sh
sbin/stop-slave.sh
sbin/stop-master.sh
```

## 🔑 Dataproc Cluster Key Concepts

### Creating a Dataproc Cluster

1. Navigate to **Dataproc** in Google Cloud Console.
2. Click **Create Cluster** -> On Compute Engine.
3. Set the **Cluster Name** (e.g., `de-zoomcamp-cluster`).
4. Choose a **Region** that matches your storage bucket location.
5. Select **Single Node** for experimentation or **Standard** for production.
6. Optional Components: **Jupyter Notebook**, **Docker**.
7. Click **Create**.

### Uploading the Spark Job to Cloud Storage

- Copy the script to Cloud Storage:

   ```sh
   gsutil cp spark_script.py gs://<BUCKET_NAME>/code/
   ```

### Submitting a Job Using the Web UI

1. Go to Dataproc/Jobs/
2. Select **Submit a Job**.
3. Choose the **Cluster** and **PySpark** as the job type.
4. Enter the Cloud Storage path to the script (`gs://<BUCKET_NAME>/code/spark_script.py`).
5. Add **arguments** for input and output paths:

    - `--input_green=gs://<BUCKET_NAME>/pq/green/2021/*`
    - `--input_yellow=gs://<BUCKET_NAME>/pq/yellow/2021/*`
    - `--output=gs://<BUCKET_NAME>/report/2021`

6. Click **Submit** and monitor job execution.

### Submitting a Job Using Google Cloud SDK

1. Assign **Dataproc Admin** role to the service account if necessary.
2. Use the following command to submit the job:

    ```bash
    gcloud dataproc jobs submit pyspark \
        --cluster=<CLUSTER_NAME> \
        --region=<REGION> \
        gs://<BUCKET_NAME>/code/python_file.py \
        -- \
            --input_arg=gs://<BUCKET_NAME>/data/* \
            --output_arg=gs://<BUCKET_NAME>/report/
    ```

## 🔑 Dataproc to BQ Key Concepts

### 1. Modify the Spark Job to Write to BigQuery

- For this, the spark_sql file is slightly modified to: [04_spark_sql_bq.py](../code/04_spark_sql_bq.py)

    ```python
    # Save the data to BigQuery
    df_result.write.format('bigquery') \
        .option('table', output) \
        .save()
    ```

### 2. Upload the Script to Google Cloud Storage

- So it can be run directly from the cloud

    ```sh
    gsutil cp your_spark_script.py gs://your-bucket/code/
    ```

### 3. Submit the Job via Dataproc

```sh
gcloud dataproc jobs submit pyspark \
    --cluster=<CLUSTER_NAME> \
    --region=<REGION> \
    gs://<BUCKET_NAME>/code/python_file.py \
    -- \
        --input_arg=gs://<BUCKET_NAME>/data/* \
        --output_arg=<PROJECT_ID>.<DATASET>.<TABLE>
```

### 4. Verify Data in BigQuery

Navigate to the BigQuery console and check if the table has been created and populated with data.

## 📚 Additional Resources

- [Storage Connector](https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage)
- [BigQuery Connector](https://cloud.google.com/dataproc/docs/concepts/connectors/bigquery)
- [BigQuery Connector PySpark](https://cloud.google.com/dataproc/docs/tutorials/bigquery-connector-spark-example#pyspark)
- [Apache Spark Standalone Mode](https://spark.apache.org/docs/latest/spark-standalone.html)
- [Google Cloud Dataproc Docs](https://cloud.google.com/dataproc/docs)
- [IAM Roles for Dataproc](https://cloud.google.com/dataproc/docs/concepts/iam)
- [Dataproc Submit a Job](https://cloud.google.com/dataproc/docs/guides/submit-job#dataproc-submit-job-gcloud)

---

| [HOME](../README.md) | [<< BACK](./5-4-notes.md) |
| -------------------- | ------------------------- |
