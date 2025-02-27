# Module 4 - Analytics Engineering
<!-- TODO : MAIN README UPDATE -->

## Before starting

> [!IMPORTANT]
> This repo is part of my experimenting and studying the material of the Data Engineering Zoomcamp.
>
> For a more detailed explanation, or if you want to follow along the DataTalks.Club DE Zoomcamp, go check their official [data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) repository for its amazing content.

## Overview

This repository provides comprehensive resources and guides for **[dbt](https://www.getdbt.com/)** (Data Build Tool), focusing on **Analytics engineering**, **data modeling**, **Testing**, and **Deployment**.

It also covers **best practices for building dbt models, setting up dbt projects, managing deployments, and ensuring data quality through testing**.

## Getting Started

### 🏁 To begin

1. Ensure you have a **[dbt Cloud](https://www.getdbt.com/)** account or install **[dbt Core](https://docs.getdbt.com/docs/core/installation-overview)** locally.
2. For dbt cloud, you can use **[dbt Cloud IDE](https://docs.getdbt.com/docs/cloud/dbt-cloud-ide/develop-in-the-cloud)**  or **[dbt Cloud CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation)** locally.
3. **SQL** knowledge and **data transformation** principles are recommended.
4. Follow the material starting from [Analytics Engineering Basics](./public_notes/4-1-1-notes.md).

> [!IMPORTANT]
>
> - Check the [Summary](#📖-summary), and **click** on the desired topic for a detailed note.
> - There's a [Navigation Menu](#navigation-menu) at the bottom for easy navigation.

## 📖 Summary

### 1. [Analytics Engineering Basics](./public_notes/4-1-1-notes.md)

#### 🎯 1.1. Key Topics

- **ETL vs ELT**: Understanding transformation workflows.
- **Dimensional Modeling**: Fact and dimension tables.
- **Best practices for analytics engineering**.

#### ⚡ 1.2. Highlights

- **Bridges data engineering and analytics** for structured reporting.
- **Uses SQL best practices** to ensure efficient data transformations.
- **Supports scalable and modular data modeling**.

---

### 2. [What is dbt?](./public_notes/4-1-2-notes.md)

#### 🎯 2.1. Key Topics

- **dbt Core vs dbt Cloud**.
- **Transforming raw data into structured datasets**.
- **Software engineering best practices in analytics**.

#### ⚡ 2.2. Highlights

- **SQL-based transformations** for efficient workflows.
- **Integrates with major data warehouses like BigQuery & Snowflake**.
- **Enables modular and reusable data models**.

---

### 3. [Setting Up dbt with BigQuery](./public_notes/4-2-1-notes.md)

#### 🎯 3.1. Key Topics

- **Initializing a dbt project in dbt Cloud**.
- **Configuring dbt settings (`dbt_project.yml`)**.
- **Running dbt commands for data transformations**.

#### ⚡ 3.2. Highlights

- **Cloud-based execution for seamless integration**.
- **Git repository integration for version control**.
- **Efficient scheduling and automation in dbt Cloud**.

---

### 4. [Setting Up dbt with Postgres](./public_notes/4-2-2-notes.md)

#### 🎯 4.1. Key Topics

- **Local setup using dbt Core with Postgres**.
- **Managing environments via `profiles.yml`**.
- **Running dbt commands for local data transformations**.

#### ⚡ 4.2. Highlights

- **Flexible local development for testing models**.
- **Supports advanced configuration with multiple environments**.
- **Ideal for self-hosted dbt workflows**.

---

### 5. [Building dbt Models](./public_notes/4-3-1-notes.md)

#### 🎯 5.1. Key Topics

- **Developing modular data models in dbt**.
- **Dependency tracking and execution order**.
- **Using `ref()` and `source()` functions**.

#### ⚡ 5.2. Highlights

- **Optimized model execution using Directed Acyclic Graphs (DAGs)**.
- **Supports ephemeral, table, and incremental materializations**.
- **Encourages modular, reusable transformations**.

---

### 6. [Testing and Documenting dbt Projects](./public_notes/4-3-2-notes.md)

#### 🎯 6.1. Key Topics

- **Defining and running dbt tests**.
- **Automating schema documentation with YAML**.
- **Using dbt Codegen for faster documentation**.

#### ⚡ 6.2. Highlights

- **Prevents faulty data from propagating to production**.
- **Ensures data integrity through unique, not-null, and relationship tests**.
- **Automates documentation with dbt’s built-in tools**.

---

### 7. [Deploying dbt in Production](./public_notes/4-4-1-notes.md)

#### 🎯 7.1. Key Topics

- **Scheduling dbt jobs in dbt Cloud**.
- **CI/CD integration for automated deployments**.
- **Monitoring jobs and debugging failures**.

#### ⚡ 7.2. Highlights

- **Automates scheduled data transformations** in production.
- **Integrates with orchestration tools like Airflow & Prefect**.
- **Enforces version control and testing for reliable deployments**.

---

## Navigation Menu

| 📌 **dbt Topics**                                               | 📜 **Description**                                                 |
|-----------------------------------------------------------------|-------------------------------------------------------------------|
| [1. Analytics Engineering Basics](./public_notes/4-1-1-notes.md) | Introduction to data modeling and engineering best practices.    |
| [2. What is dbt?](./public_notes/4-1-2-notes.md)               | Overview of dbt Core and dbt Cloud.                              |
| [3. Setting Up dbt with BigQuery](./public_notes/4-2-1-notes.md) | Cloud-based setup and execution using dbt Cloud.                |
| [4. Setting Up dbt with Postgres](./public_notes/4-2-2-notes.md) | Local setup using dbt Core with PostgreSQL.                      |
| [5. Building dbt Models](./public_notes/4-3-1-notes.md)       | Creating dbt models with modular transformations.                 |
| [6. Testing dbt Projects](./public_notes/4-3-2-notes.md)      | Implementing data validation and documentation.                  |
| [7. Deploying dbt](./public_notes/4-4-1-notes.md)            | Scheduling, CI/CD, and production best practices.                |

---

[⬆️ Back to the top](#module-4---analytics-engineering)

<!-- TODO : CHECK WHAT NEEDS TO BE DONE -->

TODO:

- [x] Update the README.md
- [x] Add the navigation menu
- [x] Add Deploy section
- [ ] Add Visualization section (not sure about this one)
