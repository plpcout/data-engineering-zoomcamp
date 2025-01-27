#!/usr/bin/env python
# coding: utf-8

import argparse
import os
from math import ceil
from time import time

import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    if url.endswith(".csv.gz"):
        csv_name = "output.csv.gz"
    else:
        csv_name = "output.csv"

    folder_path = "./files"
    csv_file_path = f"{folder_path}/{csv_name}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        # Using wget
        os.system(f"wget {url} -O {csv_file_path}")

        # Load the real file to df
        df = pd.read_csv(csv_file_path, engine="python")
        total_rows = len(df)

        # Convert text columns to datetime
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        # Prepare the column names to be used as the table schema
        schema = df.head(n=0)

        # create_engine(dialect+driver://username:password@host:port/database)
        engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

        # Test the connection
        try:
            engine.connect()
            print("Connected")
        except Exception as e:
            print(f"Connection Failed - {e}")
        engine.dispose()

        # Open connection with the DB
        with engine.connect() as conn:
            # Creates the table. If it already exists, replace.
            schema.to_sql(if_exists="replace", name=table_name, con=conn, index=False)

        # Creates an Iterator to consume the data in chunks
        chunk_size = 10000
        chunks = pd.read_csv(
            csv_file_path,
            iterator=True,
            chunksize=chunk_size,
        )

        # Total chunks
        total_chunks = ceil(total_rows / chunk_size)

        # Open connection with the DB
        with engine.connect() as conn:
            t_ini = time()
            inserted_rows = 0
            for chunk in tqdm(chunks, desc="Inserting data", unit="chunk", total=total_chunks):
                # uncomment if you want to see each chunk being printed during insertions
                # t_start = time()

                # Adjust dtypes - text to datetime
                chunk.tpep_pickup_datetime = pd.to_datetime(chunk.tpep_pickup_datetime)
                chunk.tpep_dropoff_datetime = pd.to_datetime(chunk.tpep_dropoff_datetime)

                # Insert chunk
                chunk.to_sql(if_exists="append", name=table_name, con=conn, index=False)
                inserted_rows += len(chunk)
                # Uncomment below: if you want to see each chunk being printed during insertions.
                # t_end = time()
                # print(f"Inserted {chunk_size} rows after {round(t_end - t_start, 1)} seconds.")
            t_fin = time()
            print("Connection closed")
        print(f"Job Completed - Inserted {inserted_rows} after {round(t_fin - t_ini, 1)} seconds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")

    parser.add_argument("--user", required=True, help="user name for postgres")
    parser.add_argument("--password", required=True, help="password for postgres")
    parser.add_argument("--host", required=True, help="host for postgres")
    parser.add_argument("--port", required=True, help="port for postgres")
    parser.add_argument("--db", required=True, help="database name for postgres")
    parser.add_argument(
        "--table_name", required=True, help="name of the table where we will write the results to"
    )
    parser.add_argument("--url", required=True, help="url of the csv file")

    args = parser.parse_args()

    main(args)
