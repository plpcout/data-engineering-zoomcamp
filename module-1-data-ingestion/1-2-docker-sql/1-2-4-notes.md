# Dockerizing the Ingestion Script: A Step-by-Step Guide

## Overview

This lesson demonstrates how to take a data ingestion script, previously written in [explore-ingestion.ipynb](./explore-ingestion.ipynb) notebook, and dockerize it.

By containerizing the script, we ensure portability and scalability for production workflows.

---

## Key Concepts

### 1. Converting a Notebook to a Python Script

- Use the `jupyter nbconvert` tool to convert a notebook into a `.py` script.

  ```bash
  jupyter nbconvert \
    explore-ingestion.ipynb \
    --to script \
    --output ingest_data
  ```

- Clean up the generated script by organizing imports, removing unnecessary comments, and structuring it into reusable functions.

### 2. Adding Command-Line Argument Parsing

- Use the `argparse` library to make the script configurable via command-line arguments.
- Parameters include:
  - `--user`: Database username.
  - `--password`: Database password.
  - `--host`: Database host (e.g., `localhost` or a container name).
  - `--port`: Database port.
  - `--database`: Database name.
  - `--table_name`: Target table for data.
  - `--url`: CSV file URL for data ingestion.

Example snippet for parsing arguments:

```python
import argparse

parser = argparse.ArgumentParser(description="Ingest CSV data to PostgreSQL")
parser.add_argument("--user", required=True)
parser.add_argument("--password", required=True)
parser.add_argument("--host", required=True)
parser.add_argument("--port", required=True)
parser.add_argument("--database", required=True)
parser.add_argument("--table_name", required=True)
parser.add_argument("--url", required=True)
args = parser.parse_args()
```

### 3. Downloading and Ingesting Data

- Use `wget` to download the CSV file from a given URL.
- Use `pandas` to preprocess and upload the data into PostgreSQL using SQLAlchemy.

Example command for downloading a file:

```python
import os

os.system(f"wget {args.url} -O .files/output.csv")
```

### 4. Running locally

> [!IMPORTANT]
> After all adjustments to the [ingest_data.py](./ingest_data.py) script, we are ready to run it locally passing the arguments.
---
> [!CAUTION]
> **NEVER** pass your credentials this way in a production environment.


#### Run the following command

> [!TIP]
> `--table_name=yellow_taxi_trips_local` the table name was slightly changed to explicitly identify from where this data comes.

```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips_local \
  --url=${URL}
```

### 5. Dockerizing the Script

- Create a `Dockerfile` to containerize the Python script.
- Key steps in the `Dockerfile`:
  1. Set up a base Python image.
  2. Install required Python libraries (`pandas`, `SQLAlchemy`, etc.).
  3. Add `wget` to handle file downloads.
  4. Copy the ingestion script into the container.

Example `Dockerfile`:

```dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get install -y wget

RUN pip install pandas sqlalchemy psycopg2-binary tqdm

WORKDIR /app

COPY ingest_data.py ingest_data.py

COPY ./files ./files

ENTRYPOINT ["python", "ingest_data.py"]
```

### 6. Running the Container

- Build the Docker image:

  ```bash
  docker build -t taxi_ingest:0.1 .
  ```

> [!IMPORTANT]
> It is important to remember that container's `localhost` refers to the container itself. Therefore, there will be no communication to the specified database.
>
> **Use Docker networks to enable communication between containers.**

- You can specify the network in the `docker run` command:

  ```bash
  docker run --network=pg-network ...
  ```

- Run the container with appropriate arguments:
  > [!TIP]
  > `--table_name=yellow_taxi_trips_container`  the table name was slightly changed to explicitly identify from where this data comes.

  ```bash
  URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

  docker run -it \
    --network=pg-network \
    taxi_ingest:0.1 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips_container \
    --url=${URL}
  ```

> [!IMPORTANT]
> **Handling Localhost and Container Networking**
>
> Avoid using **`localhost`** within containers, as it refers to the container itself.
> In our case, use the name of the database container
> **`--host=pg-database`**.

### 7. **Testing and Debugging**

- Drop and recreate database tables during testing to ensure data integrity.
- Use a simple HTTP server for local file hosting if downloading large files repeatedly is inefficient:

  ```bash
  python -m http.server 8000
  ```

---

## Key Takeaways

- Converting notebooks to scripts enhances reusability and portability.
- Argument parsing is critical for configurable and flexible scripts.
- Dockerizing a script ensures consistency across different environments.
- Docker networks enable seamless communication between containers.
- Proper logging and exception handling improve debugging and production readiness.
