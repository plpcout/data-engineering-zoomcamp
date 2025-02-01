# 🚀 ETL Pipeline with PostgreSQL and Kestra

## 📌 Overview

This note demonstrates how to build an **automated ETL (Extract, Transform, Load) pipeline** using **Kestra**, **PostgreSQL** and **pgAdmin** (to visualize data).

The pipeline extracts data from a public dataset, transforms it by adding unique identifiers, and loads it into a PostgreSQL database.


## 📝 Key Features

- **Automated ETL Pipelines**: Fully managed with Kestra.
- **Dynamic Inputs**: Configurable inputs to handle different datasets dynamically.
- **Database Integration**: Seamless interaction with PostgreSQL.
- **Efficient Storage Management**: Automatic file purging to save space.
- **Optimized Processing**: Conditional execution for structured workflow management.

## ⚙️ Prerequisites

Before getting started, make sure you have:

- **[Docker](https://www.docker.com/)** installed to run the containers.

## 📁 Files used in this notebook
- Compose file **[docker-compose.yml](../docker-compose.yml)**
- Kestra flow **[2-2-3-flow.yml](#)** 
<!-- TODO - add flow 2-2-3-flow.yml-->

## 🐋 Starting the Pipeline Containers.

**Start containers defined in the docker compose file**:

- Kestra, PostgreSQL, pgAdmin
- ```sh
  docker-compose up -d
  ```

## 📥 Extract Phase: Retrieving Data

### Configuring Dynamic Inputs

The workflow allows users to define parameters to be used in the pipeline:

```yaml
inputs:
  - id: taxi
    type: SELECT
    values: ["yellow", "green"]
    default: "yellow"
  - id: year
    type: SELECT
    values: ["2019", "2020", "2021"]
    default: "2019"
  - id: month
    type: SELECT
    values: ["01", "02", "03", ..., "12"]
    default: "01"
```

### Configuring Variables

```yml
variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"
  staging_table: "public_{{inputs.taxi}}_tripdata_staging"
  table: "public_{{inputs.taxi}}_tripdata"
  data: "{{outputs.extract.outputFiles[inputs.taxi ~ '_tripdata_' ~ inputs.year ~ '-' ~ inputs.month ~ '.csv']}}"
```

### Configuring Labels

```yml
- id: set_label
  type: io.kestra.plugin.core.execution.Labels
  labels:
    file: "{{render(vars.file)}}"
    taxi: "{{inputs.taxi}}"
```

### Fetching Data from Public Source

The workflow fetches datasets dynamically from this **[repository](https://github.com/DataTalksClub/nyc-tlc-data/releases)**:

```yaml
- id: extract
  type: io.kestra.plugin.scripts.shell.Commands
  outputFiles:
    - "*.csv"
  taskRunner:
    type: io.kestra.plugin.core.runner.Process
  commands:
    - wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{{inputs.taxi}}/{{render(vars.file)}}.gz | gunzip > {{render(vars.file)}}
```

## 🔄 Transform Phase: Processing Data

### Creating Database Tables

#### Staging Table (Temporary Processing Area)
- The staging table is created to hold the data before final storage:
  
  ```yaml
  - id: green_create_staging_table
    type: io.kestra.plugin.jdbc.postgresql.Queries
    sql: |
      CREATE TABLE IF NOT EXISTS {{render(vars.staging_table)}} (...);
  ```

#### Main Table (Final Storage)
- The main table is created to hold the final data:
  ```yaml
  - id: green_create_table
    type: io.kestra.plugin.jdbc.postgresql.Queries
    sql: |
      CREATE TABLE IF NOT EXISTS {{render(vars.table)}} (...);
  ```

### Loading to Staging Table

#### Truncate Staging Table

- The staging table is cleared before loading new data:

  ```yaml
  - id: green_truncate_staging_table
    type: io.kestra.plugin.jdbc.postgresql.Queries
    sql: |
      TRUNCATE TABLE {{render(vars.staging_table)}};
  ```

#### Copying Data
- The data is then loaded into the staging table:

  ```yml
  - id: green_copy_in_to_staging_table
    type: io.kestra.plugin.jdbc.postgresql.CopyIn
    columns: [column1, column2, ...]
    from: "{{render(vars.data)}}"
    header: true
    table: "{{render(vars.staging_table)}}"
    format: CSV
  ```

### Ensuring Unique Data

- Each row gets a **unique identifier** to prevent duplicates:

  ```yaml
  - id: green_add_unique_id
    type: io.kestra.plugin.jdbc.postgresql.Queries
    sql: |
      UPDATE {{render(vars.staging_table)}} SET unique_row_id = md5( desired_columns ),
      filename = '{{render(vars.file)}}';
  ```

## 📤 Load Phase: Merging Data

### Merging Staging Data into Main Table

- To prevent duplicates, data is merged conditionally:

  ```yaml
  - id: green_merge_data
    type: io.kestra.plugin.jdbc.postgresql.Queries
    sql: |
      MERGE INTO {{render(vars.table)}} AS T
      USING {{render(vars.staging_table)}} AS S
      ON T.unique_row_id = S.unique_row_id
      WHEN NOT MATCHED THEN
        INSERT (column1, column2, ...) VALUES (S.value1, S.value2, ...);
  ```

## 📊 Conditional Execution

Kestra enables **if-else logic** for structured processing. In our case, we use it to process **yellow** and **green** taxi datasets:

```yaml
- id: if_green
  type: io.kestra.plugin.core.flow.If
  condition: "{{ inputs.taxi == 'green' }}"
  then:
    # Ident the desired code blocks into the then section
    - id: green_create_table ...
    - ...
    - ...
    - ...
    - id: green_merge_data ...
```

## 🗑 File Cleanup

To **optimize storage**, the pipeline removes processed files after execution:

```yaml
- id: purge_files
  type: io.kestra.plugin.core.storage.PurgeCurrentExecutionFiles
  description: This will remove output files. Disable if you'd like to explore output files.
  disabled: false
```

## 🚀 Execution & Validation

### ▶ Running the Pipeline

1. **Execute the Kestra Flow**.
2. **Monitor Logs** using one of Kestra’s **Execution views**.
3. **Verify Data in PostgreSQL**:
- You can also check the data using **pgAdmin** at [localhost:8085](http://localhost:8085/) (check the port used in your docker-compose file).
   
   ```sql
   SELECT COUNT(*) FROM public.green_tripdata;
   ```
