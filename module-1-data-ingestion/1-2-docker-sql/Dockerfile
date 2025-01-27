FROM python:3.12-slim

RUN apt-get update && apt-get install -y wget

RUN pip install pandas sqlalchemy psycopg2-binary tqdm

WORKDIR /app

COPY ingest_data.py ingest_data.py

COPY ./files ./files

ENTRYPOINT ["python", "ingest_data.py"]
