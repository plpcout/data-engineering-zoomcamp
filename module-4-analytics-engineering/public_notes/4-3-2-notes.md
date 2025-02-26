# Testing and Documenting the dbt Project

## 📌 Overview

Ensuring data correctness is crucial in any dbt project. This section explores the importance of validating data accuracy, enforcing constraints, and providing meaningful metadata for end users through testing and documentation.

Additionally, dbt's testing framework helps prevent the propagation of incorrect data by stopping execution when tests fail, ensuring that downstream models are not built on faulty data.

## 📖 Summary

This are the main topics:

- How dbt tests work
- Types of dbt tests and how to implement them
- How dbt enforces constraints to ensure data validation
- Automating `yaml` file generation
- Maintaining project documentation using dbt’s built-in features

## 🛠️ Prerequisites

- A **dbt project** set up with a supported database (eg. [BigQuery](https://cloud.google.com/bigquery) or [PostgreSQL](https://www.postgresql.org/))
- Preloaded **trip data** (green and yellow taxi data used all over the course)
- Basic familiarity with **SQL**
- Installed **dbt dependencies** (e.g. [`dbt-core`](https://pypi.org/project/dbt-core/), [`dbt-bigquery`](https://pypi.org/project/dbt-bigquery/), or [`dbt-postgres`](https://pypi.org/project/dbt-postgres/))

## 🔑 Key Concepts

### dbt Tests

- **Definition**: Assumptions made about data that dbt validates using SQL queries.
- **Execution Logic**: If a test query returns results, the test fails, signaling data issues.
- **Default Test Types**:
  - **Unique**: Ensures a column has unique values.
  - **Not Null**: Checks that a column does not contain NULL values.
  - **Accepted Values**: Ensures a column contains only predefined values.
  - **Relationships**: Verifies foreign key constraints between tables.

### Defining Tests in YAML

- Tests are primarily defined in `schema.yml` files.
- Example of test configuration:

1. [**Not Null**](https://docs.getdbt.com/reference/resource-properties/data-tests#not_null):

    ```yml
    version: 2

    models:
      - name: orders
        columns:
          - name: order_id
            tests:
              - not_null
    ```

2. [**Unique**](https://docs.getdbt.com/reference/resource-properties/data-tests#unique):

    ```yml
    version: 2

    models:
      - name: orders
        columns:
          - name: order_id
            tests:
              - unique:
                  config:
                    where: "order_id > 21"
    ```

3. [**Accepted Values**](https://docs.getdbt.com/reference/resource-properties/data-tests#accepted_values):

    ```yml
    version: 2

    models:
      - name: orders
        columns:
          - name: status
            tests:
              - accepted_values:
                  values: ["placed", "shipped", "completed", "returned"]

          - name: status_id
            tests:
              - accepted_values:
                  values: [1, 2, 3, 4]
                  quote: false
    ```

4. [**Relationships**](https://docs.getdbt.com/reference/resource-properties/data-tests#relationships):

    ```yml
    version: 2

    models:
      - name: orders
        columns:
          - name: customer_id
            tests:
              - relationships:
                  to: ref('customers')
                  field: id
    ```

5. Custom tests: Check [**Generic tests**](https://docs.getdbt.com/best-practices/writing-custom-generic-tests).

### Running Tests

- **Run all tests**:

  ```sh
  dbt test
  ```

- **Run tests on a specific model**:

  ```sh
  dbt test --select trips
  ```

- **Run a single test**:

  ```sh
  dbt test --select test_name
  ```

### Automating YAML File Generation

- The [`dbt-codegen`](https://github.com/dbt-labs/dbt-codegen) package can generate `schema.yml` files automatically.
- Example command to generate model YAML:

  ```sh
  dbt run-operation generate_model_yaml --args '{"models": ["trips"]}'
  ```

### Documentation in dbt

- dbt enables automatic documentation generation using metadata from YAML files.
- **Generate documentation**:

  ```sh
  dbt docs generate
  ```

- **Serve documentation locally**:

  ```sh
  dbt docs serve
  ```

- The documentation includes:
  - Model descriptions
  - Column descriptions
  - Test definitions
  - Data lineage diagrams

## 🚀 Execution Flow

1. **Run dbt tests** to ensure data integrity.
2. **Generate documentation** to provide metadata for stakeholders.
3. **Use dbt docs** to explore data lineage and model details.

## 📚 Additional Resources

- [dbt Documentation](https://docs.getdbt.com/)
- [dbt Codegen Package](https://github.com/dbt-labs/dbt-codegen)
- [dbt Testing](https://docs.getdbt.com/reference/resource-properties/data-tests)
- [dbt Testing Best Practices](https://docs.getdbt.com/docs/building-a-dbt-project/tests)

---

| [HOME](../README.md) | [<< BACK](./4-3-1-notes.md) |
| -------------------- | --------------------------- |
