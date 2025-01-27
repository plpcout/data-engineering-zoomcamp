# Docker-SQL Repository

## Overview

The instructions in this repository provide guides and resources for setting up and managing PostgreSQL databases using Docker, along with key SQL concepts and practices for data engineering workflows.

## Getting Started

### To begin

1. Ensure you have Docker installed. [Download Docker](https://www.docker.com/).
2. Follow the material starting on [1.2.1](./public_notes/1-2-1-notes.md).

> [!IMPORTANT]
>
> - Check the [Summary](#summary), and click on the desired topic for a detailed note.
> - Theres a [Navigation Menu](#navigation-menu) on the bottom for easy navigation.

## Summary

### 1. [Introduction to Docker](./public_notes/1-2-1-notes.md)

#### 1.1. Key Topics

- What is Docker and why use it?
- Testing Docker installation with `hello-world` and Ubuntu containers.
- Running Python containers interactively.
- Creating and customizing Docker images with `Dockerfile`.
- Building and running simple Python-based data pipelines.

#### 1.2. Highlights

- **Reproducibility**: Isolate dependencies and applications using containers.
- **Step-by-Step Guides**: Learn how to create Docker images for specific tasks, like running Python scripts.
- **Practical Application**: Build basic data pipelines to understand the interaction between Docker and Python.

---

### 2. [Setting Up PostgreSQL with Docker and Loading Data](./public_notes/1-2-2-notes.md)

#### 2.1. Key Topics

- Setting up PostgreSQL in Docker with environment variables and mapped volumes.
- Connecting to PostgreSQL using tools like `pgcli` and SQLAlchemy.
- Preprocessing large datasets using Pandas.
- Loading data into PostgreSQL in chunks for efficient ingestion.

#### 2.2. Highlights

- **Detailed Setup Instructions**: Configure PostgreSQL with persistent data storage.
- **Efficient Data Handling**: Use chunked insertion to manage large datasets.
- **Hands-On Examples**: Preprocess and load the NYC Taxi dataset into a PostgreSQL database.

---

### 3. [Connecting pgAdmin and Postgres with Docker](./public_notes/1-2-3-notes.md)

#### 3.1. Key Topics

- Setting up pgAdmin as a graphical interface for PostgreSQL.
- Creating a Docker network for inter-container communication.
- Configuring pgAdmin to connect to a PostgreSQL container.
- Exploring and managing databases through the pgAdmin interface.

#### 3.2. Highlights

- **User-Friendly Interface**: Use pgAdmin to visualize and manage database queries.
- **Network Configuration**: Ensure seamless communication between containers.
- **Database Exploration**: Navigate schemas and execute SQL queries directly from the interface.

---

### 4. [Dockerizing the Ingestion Script: A Step-by-Step Guide](./public_notes/1-2-4-notes.md)

#### 4.1. Key Topics

- Converting Jupyter notebooks to Python scripts with `jupyter nbconvert`.
- Adding command-line argument parsing for script flexibility.
- Creating a Docker image to containerize the ingestion script.
- Running the script in a Docker container with real-world data.

#### 4.2. Highlights

- **Script Reusability**: Transform notebooks into modular scripts.
- **Production-Ready Workflows**: Dockerize scripts to ensure portability.
- **Practical Examples**: Ingest data into PostgreSQL directly from the containerized script.

---

### 5. [Running PostgreSQL and pgAdmin with Docker Compose](./public_notes/1-2-5-notes.md)

#### 5.1. Key Topics

- Understanding Docker Compose and its benefits for multi-container setups.
- Configuring `docker-compose.yaml` to run PostgreSQL and pgAdmin.
- Simplifying container orchestration and dependency management.

#### 5.2. Highlights

- **Streamlined Workflows**: Manage multiple containers with a single command.
- **Networking Made Easy**: Enable seamless communication between services in a Compose setup.
- **Accessible Interfaces**: Quickly access PostgreSQL and pgAdmin after starting services.

---

### 6. [SQL Refresher: Joins, Grouping, and Aggregations](./public_notes/1-2-6-notes.md)

#### 6.1. Key Topics

- Different types of SQL joins: inner, left, right, and outer.
- Grouping data and using aggregate functions (e.g., COUNT, SUM).
- Data validation techniques to handle edge cases.

#### 6.2. Highlights

- **SQL Mastery**: Strengthen your understanding of joins and aggregations.
- **Data Analysis Skills**: Learn to group and summarize data effectively.
- **Real-World Examples**: Practical SQL queries for analytics and validation.

---

## Navigation Menu

| **Notes**                                                              | **Description**                                                        |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [1. Introduction to Docker](./public_notes/1-2-1-notes.md)             | The basics of Docker / Setup testing / Creating the first pipeline.    |
| [2. Setting up PostgreSQL with Docker](./public_notes/1-2-2-notes.md)  | Set up PostgreSQL with Docker / Ingesting large datasets using Pandas. |
| [3. pgAdmin and PostgreSQL with Docker](./public_notes/1-2-3-notes.md) | Using pgAdmin for managing PostgreSQL databases in Docker.             |
| [4. Dockerizing the Ingestion Script](./public_notes/1-2-4-notes.md)   | Converting the ingestion script into a Dockerized application.         |
| [5. Docker Compose](./public_notes/1-2-5-notes.md)                     | Simplify container management for PostgreSQL and pgAdmin.              |
| [6. SQL Refresher](./public_notes/1-2-6-notes.md)                      | Review SQL concepts, including joins, grouping, and aggregations.      |

---

[Back to the top](#docker-sql-repository)
