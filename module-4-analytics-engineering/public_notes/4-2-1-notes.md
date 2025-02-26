# Setting Up a dbt Project with BigQuery and dbt Cloud (Cloud Approach)

## 📌 Overview

This section outlines the process of setting up a **dbt** project from scratch using **BigQuery** and **dbt Cloud**.

## 📖 Summary

Topics covered:

- Initializing a **dbt project** using **dbt CLI** or **dbt Cloud**.
- Configuring **`dbt_project.yml`** for project settings.
- Setting up **repository integration** and working with **branches**.
- Running **dbt commands** to validate and execute the project.

## 🛠️ Prerequisites

- A **GitHub** or other Git provider repository
- A **dbt Cloud** account
- Basic knowledge of **Git**
- Installed **dbt CLI** (if using the command line approach)

## 🚀 Project Initialization

### Creating a New dbt Project

A **dbt project** includes a predefined structure with essential configuration files.

**Methods to initialize:**

- **Using dbt CLI**:

  ```sh
  dbt init <project_name>
  ```

  This generates the necessary files and folders.
- **Using dbt Cloud**:
  - The web-based IDE provides a guided setup process.

### Configuring the Project

- The **`dbt_project.yml`** file is automatically generated.
- Defines the **project name**, **database connections**, and **global settings**.
- Can be customized for **folder structure** and **naming conventions**.

## 🔗 Repository Setup

- dbt requires integration with a **Git repository**.
- The project should be placed under a **version-controlled directory**.
- Ensure the **correct branch** is used before making changes.

### Managing Branches

- New development should be done in a **dedicated branch**.
- The **main branch** should remain stable and should not be directly modified.

## 📌 Working with dbt Models

### Project Structure

- The project contains predefined folders for **models, tests, and configurations**.
- Example models are included, which can be **modified or removed**.

### Running dbt Commands

- **Build the project**:

  ```sh
  dbt build
  ```

- **Install dependencies**:

  ```sh
  dbt deps
  ```

- **Run models and materialize tables**:

  ```sh
  dbt run
  ```

## 🌐 Commit and Deployment

- Ensure all changes are **committed** to the repository.
- Use **meaningful commit messages** for tracking progress.
- Validate the setup before proceeding with model development.

## 📚 Additional Resources

- [dbt Documentation](https://docs.getdbt.com/)
- [dbt Cloud Setup](https://docs.getdbt.com/docs/get-started-dbt#dbt-cloud)

---

| [HOME](../README.md) | [<< BACK](./4-1-2-notes.md) | [NEXT >>](./4-2-2-notes.md) |
| -------------------- | --------------------------- | --------------------------- |
