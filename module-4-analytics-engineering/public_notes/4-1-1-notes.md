# Analytics Engineering Basics

## 📌 Overview

Analytics engineering bridges the gap between data engineering and data analysis. It incorporates software engineering best practices into the work of data analysts and data scientists while ensuring that data is structured for efficient querying and business use.

---

## ✅ Prerequisites

- Basic understanding of cloud data warehouses (e.g., [BigQuery](https://cloud.google.com/bigquery/docs), [Snowflake](https://docs.snowflake.com/), [Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html))
- Familiarity with **ETL** (Extract, Transform, Load) and **ELT** (Extract, Load, Transform) processes
- Knowledge of **SQL** and data modeling concepts
- Experience with **BI tools** (e.g., [Looker](https://cloud.google.com/looker), [Mode](https://mode.com/), [Google Data Studio](https://datastudio.google.com/))

---

## 🎯 Key Concepts

### The Role of an Analytics Engineer

- Combines best practices from **software engineering** and **data workflows**.
- Ensures data analysts and scientists have **reliable, structured data**.
- Works with **data loading, storage, transformation, and presentation tools**.

### ETL vs. ELT

| Process | Description                | Advantages                                                                   |
| ------- | -------------------------- | ---------------------------------------------------------------------------- |
| **ETL** | Extract → Transform → Load | Ensures clean, structured, and compliant data but takes longer to implement. |
| **ELT** | Extract → Load → Transform | Leverages cloud storage and compute for flexibility and speed.               |

### Dimensional Modeling

- **Fact Tables**: Store **metrics** and **business process measurements** (e.g., sales, orders).
- **Dimension Tables**: Provide **context** to fact tables (e.g., customers, products).
- Uses **Star Schema** for **efficient querying** and performance.

### Kitchen Analogy for Data Processing 🍽️

| Data Process          | Analogy             | Description                                                  |
| --------------------- | ------------------- | ------------------------------------------------------------ |
| **Staging Area**      | Ingredients Storage | Raw data is stored and not directly accessible to end users. |
| **Processing Area**   | Kitchen             | Data is transformed, ensuring consistency and structure.     |
| **Presentation Area** | Dining Hall         | Final transformed data is presented to stakeholders.         |
