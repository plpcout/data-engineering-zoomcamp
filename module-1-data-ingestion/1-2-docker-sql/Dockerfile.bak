FROM python:3.12-slim

RUN pip install pandas

WORKDIR /app

# COPY pipeline.py pipeline.py
COPY pipeline_args.py pipeline_args.py

# ENTRYPOINT ["bash"]
ENTRYPOINT ["python", "pipeline_args.py"]
