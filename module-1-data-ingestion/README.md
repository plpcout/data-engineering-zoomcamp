# Module 1 - Data Ingestion

[![Python](https://img.shields.io/badge/Python-3.13-4B8BBE.svg?style=flat&logo=python&logoColor=FFD43B&labelColor=3776AB)](https://www.python.org/)
[![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform&logoColor=fff&style=flat)](https://www.terraform.io/)
[![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat&logo=googlecloud&logoColor=fff&labelColor=4285F4)](https://cloud.google.com/)
[![Docker](https://img.shields.io/badge/docker-2496ED?style=flat&logo=docker&logoColor=fff&labelColor=2496ED)](https://www.docker.com/)
![Postgres](https://img.shields.io/badge/postgres-4169E1.svg?style=flat&logo=postgresql&logoColor=FFF&labelColor=4169E1)
[![pgAdmin](https://img.shields.io/badge/pgAdmin-23456A?style=flat&logo=pgadmin&logoColor=fff&labelColor=23456A)](https://www.pgadmin.org/)


## Before starting

> [!IMPORTANT]
> This repo is part of my experimenting and studying the material of the Data Engineering Zoomcamp.
>
> For a more detailed explanation, or if you want to follow along the DataTalks.Club DE Zoomcamp, go check their official [data-enginering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) repository for its amazing content.

## Getting Started

1. Infrastructure as Code with Terraform - Start [Here](./1-1-terraform-gcp/README.md).
2. Data Ingestion with Docker Containers & SQL - Start [Here](./1-2-docker-sql/README.md).

## Developer Setup

**1.** Instal dependencies on pyproject.toml:

```shell
uv sync
```

**2.** Activate the virtual environment create by uv:

```shell
source .venv/bin/activate
```

**3.** (Optional) Install pre-commit:

```shell
pip install pre-commit

pre-commit install
```
