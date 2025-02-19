# Setting Up a dbt Project with Postgres and dbt Core (Local Approach)

## 📌 Overview

This section provides a step-by-step approach to setting up a **dbt** project using **Postgres** and **dbt Core** locally. It covers project initialization, database configuration, and repository setup.

## 📖 Summary

This guide covers:

- Initializing a **dbt project** locally using **dbt Core** and **Postgres**.
- Configuring **`profiles.yml`** to establish database connections.
- Managing different **environments** within the project.
- Running **dbt commands** to validate and execute the project.

## 🛠️ Prerequisites

- A **GitHub** or other Git provider repository
- A **PostgreSQL** database (local or remote)
- Installed **dbt Core**
- Basic knowledge of **Git**
- Installed **Postgres adapter** for dbt

## 🚀 Project Initialization

### Creating a New dbt Project

A **dbt project** consists of essential configuration files and folders.

**Steps to initialize:**

- **Create a new repository** to store the project.
- **Clone the repository locally**:
  ```sh
  git clone <repository_url>
  ```
- **Navigate to the project directory** and run:
  ```sh
  dbt init <project_name>
  ```
  This generates the required files and folders.

### Configuring the Project

- The **`dbt_project.yml`** file is created automatically.
- Defines **project settings**, **database connections**, and **global configurations**.
- The **profile name** must match the one in `profiles.yml`.

## 🔑 Database Configuration

### Setting Up the Postgres Profile

- The **`profiles.yml`** file manages **database connections**.
- This file is located at `~/.dbt/profiles.yml`.
- Example Postgres configuration:
  ```yaml
  my_postgres_profile:
    target: dev
    outputs:
      dev:
        type: postgres
        host: localhost
        user: my_user
        password: my_password
        port: 5432
        dbname: production
        schema: dbt_models
        threads: 4
  ```
- Ensure the **profile name** in `dbt_project.yml` matches `my_postgres_profile`.

### Switching Between Environments

- Different **targets** can be defined within `profiles.yml`.
- Example additional **sandbox** environment:
  ```yaml
  sandbox:
    type: postgres
    host: localhost
    user: sandbox_user
    password: sandbox_pass
    port: 5432
    dbname: sandbox_db
    schema: sandbox_models
    threads: 2
  ```
- Switch environments by modifying the `target` value.

## 🔑 Working with dbt Models

### Project Structure

- The project contains predefined folders for **models, tests, and configurations**.
- Example models are included and can be modified or removed.

### Running dbt Commands

- **Check database connection**:
  ```sh
  dbt debug
  ```
- **Build the project**:
  ```sh
  dbt build
  ```
- **Run models and materialize tables**:
  ```sh
  dbt run
  ```
- **Install dependencies**:
  ```sh
  dbt deps
  ```

## 🌐 Commit and Deployment

- Ensure all changes are **committed** to the repository.
- Use **descriptive commit messages** for better tracking.
- Validate setup before starting model development.

## 📚 Additional Resources

- [dbt Documentation](https://docs.getdbt.com/)
- [dbt Core Setup](https://docs.getdbt.com/docs/get-started-dbt#dbt-core)
