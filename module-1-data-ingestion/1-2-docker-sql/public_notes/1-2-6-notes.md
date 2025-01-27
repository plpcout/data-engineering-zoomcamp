# SQL Refresher: Joins, Grouping, and Aggregations

## Overview

This notes covers a refresher on SQL concepts, focusing on joins, grouping, and aggregations. These are essential tools for data analysis and are particularly relevant for analytics engineering workflows like those in [dbt](https://www.getdbt.com/).

## Key Concepts

### 1. Database Setup

- You should have two key tables loaded in your database:
  - **`yellow_taxi_trips`**
    - This table should be already loaded. If not, run [ingest_data.py](./ingest_data.py) script.
  - **`zones`**
    - If you don't have this table loaded yet, run the [ingest_zones.py](./ingest_zones.py) script.

### 2. Joins in SQL

Joins combine data from multiple tables. Here are the main types:

- **Inner Join**
  Matches rows from two tables where a specific condition is met.

  ```sql
  SELECT
      tpep_pickup_datetime,
      tpep_dropoff_datetime,
      total_amount,
      CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
      CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropff_loc"
  FROM
      yellow_taxi_trips t,
      zones zpu,
      zones zdo
  WHERE
      t."PULocationID" = zpu."LocationID"
      AND t."DOLocationID" = zdo."LocationID"
  LIMIT 100;
  ```

  - Only rows with matching the **location ID** in both tables appear in the result.

- **Left Join**
  Includes all rows from the left table, even if there’s no match in the right table.

  ```sql
  SELECT
      tpep_pickup_datetime,
      tpep_dropoff_datetime,
      total_amount,
      CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
      CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropff_loc"
  FROM
      yellow_taxi_trips t
  LEFT JOIN
      zones zpu ON t."PULocationID" = zpu."LocationID"
  JOIN
      zones zdo ON t."DOLocationID" = zdo."LocationID"
  LIMIT 100;
  ```

  - Non-matching rows in the right table result in `NULL` values.

- **Right Join**
  Includes all rows from the right table, even if there’s no match in the left table.

  ```sql
  SELECT
      tpep_pickup_datetime,
      tpep_dropoff_datetime,
      total_amount,
      CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
      CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropff_loc"
  FROM
      yellow_taxi_trips t
  RIGHT JOIN
      zones zpu ON t."PULocationID" = zpu."LocationID"
  JOIN
      zones zdo ON t."DOLocationID" = zdo."LocationID"
  LIMIT 100;
  ```

  - Non-matching rows in the left table result in `NULL` values.

- **Outer Join**
  Combines both left and right join behavior to show all rows from both tables, with `NULL` for non-matching rows.

  ```sql
  SELECT
      tpep_pickup_datetime,
      tpep_dropoff_datetime,
      total_amount,
      CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
      CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropff_loc"
  FROM
      yellow_taxi_trips t
  OUTER JOIN
      zones zpu ON t."PULocationID" = zpu."LocationID"
  JOIN
      zones zdo ON t."DOLocationID" = zdo."LocationID"
  LIMIT 100;
  ```

### 3. Grouping and Aggregations

Grouping enables summarizing data, often combined with aggregate functions like `COUNT`, `SUM`, `MAX`, etc.

- **Basic Grouping by Day**
  Example: Count trips per day.

  ```sql
  SELECT
      CAST(tpep_dropoff_datetime AS DATE) AS "day",
      COUNT(1) AS "trips"
  FROM
      yellow_taxi_trips t
  GROUP BY
      CAST(tpep_dropoff_datetime AS DATE)
  LIMIT 100;
  ```

- **Multiple Grouping**
  Grouping by multiple fields for granular analysis:

  ```sql
  SELECT
      DATE_TRUNC('day', t."tpep_dropoff_datetime") AS "trip_date",
      t."PULocationID",
      COUNT(*) AS "trip_count",
      SUM(t."total_amount") AS "total_amount"
  FROM
      yellow_taxi_trips t
  GROUP BY
      1, 2
  ORDER BY
      "trip_date" ASC,
      t."PULocationID" ASC;
  ```

### 4. Data Validation and Edge Cases

- Check for missing data:

  ```sql
  SELECT
      *
  FROM
      yellow_taxi_trips
  WHERE
      "PULocationID" IS NULL;
  ```

- Use `NOT IN` to find IDs in one table that don’t exist in another:

  ```sql
  SELECT
      t."PULocationID"
  FROM
      yellow_taxi_trips t
  WHERE
      t."PULocationID" NOT IN
          (SELECT z."LocationID" FROM zones z);
  ```

### 5. Key Takeaways

- **Joins and Grouping**: Fundamental for data transformations and aggregations in analytics.
- **Best Practices**: Always validate data (e.g., check for `NULL` values, orphan IDs).
- **SQL Agility**: Experiment with joins, group by multiple fields, and use aggregate functions to uncover deeper insights.

---

| [HOME](../README.md) | [<< BACK](./1-2-5-notes.md) |
| -------------------- | ---------------------------- |
