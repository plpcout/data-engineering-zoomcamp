# Setting Up PostgreSQL with Docker and Loading Data

## Overview

This is a summary of the process of setting up a PostgreSQL database using Docker, configuring it for local development, and loading data into it using Python and Pandas.

> [!TIP]
> Commented notebook with all the code [explore-ingestion.ipynb](explore-ingestion.ipynb)

## Key Concepts

### Setting Up PostgreSQL in Docker

- **Docker Image**: Use the official PostgreSQL Docker image (`postgres:13`).
- **Environment Variables**: Configure PostgreSQL using environment variables:
  - `POSTGRES_USER`: Database user (e.g., `root`).
  - `POSTGRES_PASSWORD`: Password for the user (e.g., `root`).
  - `POSTGRES_DB`: Database name (e.g., `ny_taxi`).
- **Volumes**:
  - Map a folder from the host machine to the container to persist data across sessions.
  - Syntax: `-v /host/path:/container/path`.
- **Ports**: Map the default PostgreSQL port `5432` from the container to the host machine for database access.

- **Docker Run example**:

  ```bash
  docker run -it \
    --name postgres-container \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/../ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres:13
  ```

- **Stopping the container**:

  ```bash
  docker stop postgres-container
  ```

- **Starting the container**:

  ```bash
  docker start postgres-container
  ```

### Connecting to PostgreSQL

- **CLI Tool**: Use `pgcli`, a Python-based command-line client for PostgreSQL. Install via `pip install pgcli`.
- **Connecting**:

  ```bash
  pgcli -h localhost -p 5432 -u root -d ny_taxi
  ```

### Exploring the Dataset

- **Dataset**: Use the NYC Taxi dataset (e.g., yellow taxi trip records from January 2021).
- **Preprocessing**:
  - Use utilities like `head` to inspect a subset of the data.
  - Ensure compatibility with large datasets by chunking.

### Loading Data into PostgreSQL

- **Data Transformation with Pandas**:
  - Use `pandas.to_datetime()` to convert string columns to timestamps.
  - Generate SQL table schemas using `pandas.io.sql.get_schema()`.
- **Database Connection**: Establish a connection using SQLAlchemy:

  ```python
  from sqlalchemy import create_engine
  engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")
  ```

- **Chunked Insertion**:

  - Read the dataset in chunks using Pandas iterators (`chunk_size=100000`).
  - Create the table using the `head(n=0)` to get the column names.

    > **Atention**: The table will be **created** if it doesn't exist or **replaced** if it already exists

    ```python
    df.head(n=0).to_sql('table_name', engine, if_exists='replace', index=False)
    ```

  - Insert data into PostgreSQL in batches to avoid memory issues:

    ```python
    df.to_sql('table_name', engine, if_exists='append', index=False)
    ```

### Key Takeaways

- Use Docker to run PostgreSQL for local development.
- Persist data using Docker volumes and map host-container ports for accessibility.
- Preprocess large datasets with Pandas and load them efficiently into PostgreSQL using chunks.

---

## Extra - Connecting to Postgres with Jupyter and Pandas

This is an alternative method to connect to a Postgres database using Jupyter notebooks and Pandas. It allows you to interact with the database in a Pythonic and user-friendly way, other than using the CLI tool `pgcli`.

Commented notebook with all the code [pg-test-connection.ipynb](pg-test-connection.ipynb)

### Prerequisites

- Ensure Postgres is running (e.g., via Docker).
- Your target table should exist in the Postgres database `yellow_taxi_data`
- Required Python packages:

  ```bash
  pip install sqlalchemy psycopg2-binary pandas
  ```

### Establishing a Connection

- Use SQLAlchemy to connect to the Postgres database:

  ```python
  from sqlalchemy import create_engine

  # Replace with your credentials
  connection_string = "postgresql://username:password@host:port/database"
  engine = create_engine(connection_string)

  # Test the connection
  with engine.connect() as connection:
      print("Connection successful!")
  ```

### Querying Data

- Run SQL queries and load results into a Pandas DataFrame:

  ```python
  import pandas as pd

  query = "SELECT 1;"  # Simple query to test the connection
  df = pd.read_sql(query, engine)
  print(df)
  ```

### Listing Tables

- The `\dt` command in `pgcli` does not work in standard SQL. Use an equivalent query to list tables:

  ```python
  query = """
    SELECT table_name FROM information_schema.tables
    WHERE table_schema = 'public';
    """

  tables = pd.read_sql(query, engine)
  print(tables)
  ```

### Inserting Data (optional)

- > [!TIP] > **If you still have your Postgress table, you can skip this section**

- Insert a Pandas DataFrame into a Postgres table:

  ```python
  df.to_sql("table_name", engine, if_exists="replace", index=False)
  ```

### Retrieving Data

- Query specific data from a table and load it into a DataFrame:

  ```python
  query = "SELECT * FROM table_name LIMIT 10;"
  result_df = pd.read_sql(query, engine)
  print(result_df)
  ```
