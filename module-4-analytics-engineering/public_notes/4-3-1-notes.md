# Build the First dbt Models

## 📌 Overview

This section covers the development of initial dbt models, focusing on modular data modeling, transformations, and configurations in a dbt project.

## 📖 Summary

This document provides a structured approach to creating dbt models, covering key concepts like:

- Data sources.
- Materializations.
- Modular modeling techniques.
- Macros, variables.
- Best practices for managing transformations efficiently.

## 🛠️ Prerequisites

- A **dbt project** set up with a supported database (eg. [BigQuery](https://cloud.google.com/bigquery) or [PostgreSQL](https://www.postgresql.org/))
- Preloaded **trip data** (green and yellow taxi data used all over the course)
- Basic familiarity with **SQL**
- Installed **dbt dependencies** (e.g. [`dbt-core`](https://pypi.org/project/dbt-core/), [`dbt-bigquery`](https://pypi.org/project/dbt-bigquery/), or [`dbt-postgres`](https://pypi.org/project/dbt-postgres/))

## 🔑 Key Concepts

### Dependency Resolution and Execution Order

- **Dependency Tracking**: dbt automatically determines dependencies between models using the `ref()` function.
- **Directed Acyclic Graph (DAG)**: dbt structures execution using a DAG, ensuring models run in the correct sequence.
- **Selective Execution**: Commands like `dbt run --select model_name+` execute models along with their dependents.
- **Build Strategy**: dbt first tests source freshness, runs transformations, and then executes final models in the appropriate order.

### dbt Models

- **Definition**: SQL files that define transformations.
- **Structure**: Uses `SELECT` statements while dbt handles DDL/DML operations.
- **Materialization Types**:
  - **Ephemeral**: Temporary, referenced only within other models.
  - **View**: Defined as a SQL view.
  - **Table**: Fully materialized table.
  - **Incremental**: Updates existing tables instead of full recreation.

### Sources and Seeds

- **Sources**: External tables loaded into the warehouse, referenced in YAML files.

  - e.g.

    ```yml
    sources:
        - name: <source_name>
        database: "<project_id>"
        schema: "<dataset_name>"

        tables:
        - name: green_tripdata
        - name: yellow_tripdata
    ```

- **Seeds**: CSV files stored in the dbt project repository and imported for use.
- Defining sources and seeds in **YAML** abstracts complexity and enables better testing.

### Model Referencing

- **`source()` function**: References external sources.
- **`ref()` function**: References dbt models, ensuring compatibility across environments.
- **Dependency tracking**: Ensures correct execution order.

### Testing and Data Quality

- **Source freshness tests** ensure data updates within defined thresholds.
- **Custom tests** check for nulls, uniqueness, and referential integrity.
- dbt’s testing framework maintains high data quality standards.

### Macros and Jinja Templating

- **Jinja** allows for dynamic SQL generation.
- **Macros** function as reusable code blocks, similar to SQL functions.

  ```sql
  -- This macro returns the description of the payment_type
  {% macro get_payment_type_description(payment_type) %}
      case {{ dbt.safe_cast("payment_type", api.Column.translate_type("integer")) }}
          when 1 then 'Credit card'
          when 2 then 'Cash'
          when 3 then 'No charge'
          when 4 then 'Dispute'
          when 5 then 'Unknown'
          when 6 then 'Voided trip'
          else 'EMPTY'
      end
  {% endmacro %}
  ```

- **Example Usage**:

  ```sql
  {{ get_payment_type_description(payment_type) }}
  ```

  - Abstracts logic for mapping payment type codes to descriptions.

### Variables

- **Can be defined at project level** and used within models.
- **Example Usage**:

  ```sql
  {% if var('is_test_run', default=true) %}
    LIMIT 100
  {% endif %}
  ```

  - Helps test with smaller datasets before full execution.

### Packages

- **dbt packages** act as libraries containing reusable macros and models.
- **Internal Company Packages**: dbt allows organizations to create internal packages for shared macros, tests, and transformations, enabling reuse across multiple projects.
- **Example**: Using [`dbt_utils.generate_surrogate_key()`](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) to create unique identifiers.
- Packages are added via `packages.yml`

  ```yaml
  packages:
  - package: dbt-labs/dbt_utils
      version: 1.3.0
  - package: dbt-labs/codegen
      version: 0.13.1
  ```

- Install it with:

  ```bash
  dbt deps
  ```

## ⚙️ Project Structure

```
├── macros
│   ├── get_payment_type_description.sql
├── models
│   ├── core
│   │   ├── dim_zones.sql
│   │   ├── fact_trips.sql
│   ├── staging
│   │   ├── staging_green_trip_data.sql
│   │   ├── staging_yellow_trip_data.sql
├── seeds
│   ├── taxi_zone_lookup.csv
├── dbt_project.yml
├── packages.yml
```

## 🚀 Execution

### Most Common Commands for running the Project

- **Compile all models**:

  ```sh
  dbt compile
  ```

- **Build all models**:

  ```sh
  dbt build
  ```

- **Run a specific model**:
  ```sh
  dbt run --select fact_trips
  ```
- **Execute with full data**:

  ```sh
  dbt build --vars '{"is_test_run": "false"}'
  ```

- **Run models with dependencies**:
  ```sh
  dbt build --select +fact_trips
  ```

## 📚 Additional Resources

- [dbt Documentation](https://docs.getdbt.com/)
- [dbt Utils Package](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/)
- [dbt codegen Package](https://hub.getdbt.com/dbt-labs/codegen/latest/)
- [Jinja Templating](https://jinja.palletsprojects.com/)
