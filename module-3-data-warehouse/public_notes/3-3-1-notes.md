# BigQuery Machine Learning

## 📌 Overview

This section explains how to leverage **BigQuery ML** to create machine learning models directly within Google BigQuery using **SQL**. This approach allows you to build, evaluate, and deploy models without needing to export data to external systems or rely on other programming languages like `Python` or `Java`. The aim is to show how easy it can be to integrate machine learning directly into data operations.

## 📋 Prerequisites

For reproducing the code, ensure the requirements are in place:

- A **Google Cloud** account with access to **BigQuery**.
- Basic knowledge of **SQL** and minor **machine learning** principles.
- A **dataset** stored in BigQuery, which will be used to train the model. (NY Taxi Data)

## 🔑 Key Terms

- **BigQuery ML**: A tool within BigQuery that enables machine learning capabilities using SQL queries.
- **Feature Engineering**: The transformation of raw data into meaningful features used for model training.
- **Hyperparameter Tuning**: The process of adjusting a model's hyper parameters to enhance performance.

## 🛠️ Hands-on

### 1. Prepare Your Data

Before building a machine learning model, it's important to prepare your data. Begin by selecting the relevant columns from your dataset and filtering out any rows with invalid or missing values. The following SQL query selects specific columns from the `yellow_tripdata_partitioned` table, filtering out rows where `fare_amount` equals zero:

```sql
-- SELECT THE COLUMNS INTERESTED FOR YOU
SELECT passenger_count, trip_distance, PULocationID, DOLocationID, payment_type, fare_amount, tolls_amount, tip_amount
FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitioned` WHERE fare_amount != 0;
```

### 2. Create a Machine Learning Table

After selecting the relevant data, you can create a machine learning-compatible table with proper data types. This step ensures that the system can process and train on the dataset.

The `PULocationID`, `DOLocationID`, and `payment_type` fields are cast from **INTEGER** to **STRING** to ensure proper feature engineering by BigQuery:

- In this case
  Category feature: `PULocationID`, `DOLocationID`, and `payment_type`

```sql
-- CREATE A ML TABLE WITH APPROPRIATE TYPE
CREATE OR REPLACE TABLE `taxi-rides-ny.nytaxi.yellow_tripdata_ml` (
  `passenger_count` INTEGER,
  `trip_distance` FLOAT64,
  `PULocationID` STRING,
  `DOLocationID` STRING,
  `payment_type` STRING,
  `fare_amount` FLOAT64,
  `tolls_amount` FLOAT64,
  `tip_amount` FLOAT64
) AS (
  SELECT
    passenger_count,
    trip_distance,
    cast(PULocationID AS STRING),
    CAST(DOLocationID AS STRING),
    CAST(payment_type AS STRING),
    fare_amount,
    tolls_amount,
    tip_amount
  FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitioned`
  WHERE fare_amount != 0
);
```

### 3. Build the Machine Learning Model

Once the data is prepared, the next step is to build the machine learning model. This is done through a simple SQL command that sets the model type and defines the label column, which in this case is `tip_amount`. Here's an example of how to create a **linear regression** model:

```sql
-- CREATE MODEL WITH DEFAULT SETTING
CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_model`
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['tip_amount'],
  DATA_SPLIT_METHOD='AUTO_SPLIT') AS
SELECT
  *
FROM
  `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
  tip_amount IS NOT NULL;
```

This query sets the model type to `linear_reg` and automatically splits the data into training and evaluation datasets. The model is trained to predict the `tip_amount`.

### 4. Check Features

After the model is trained, you may want to explore which features were most influential in building the model. Use the `FEATURE_INFO` function to retrieve detailed information about the features:

```sql
-- CHECK FEATURES
SELECT * FROM ML.FEATURE_INFO(MODEL `taxi-rides-ny.nytaxi.tip_model`);
```

This provides a summary of each feature, including the type of data and statistical properties that could influence model behavior.

### 5. Evaluate the Model

Evaluation metrics such as **Mean Absolute Error** and **Mean Squared Error** help gauge how well the model performs. The following query compares predictions to actual values, providing key evaluation metrics:

```sql
-- EVALUATE THE MODEL
SELECT
  *
FROM
  ML.EVALUATE(MODEL `taxi-rides-ny.nytaxi.tip_model`,
  (
    SELECT
      *
    FROM
      `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
      tip_amount IS NOT NULL
  ));
```

These metrics give you an objective measure of model performance.

### 6. Make Predictions

Once you've trained and evaluated the model, you can use it to make predictions on unseen data. This query predicts `tip_amount` for each record in the dataset:

```sql
-- PREDICT THE MODEL
SELECT
  *
FROM
  ML.PREDICT(MODEL `taxi-rides-ny.nytaxi.tip_model`,
  (
    SELECT
      *
    FROM
      `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
      tip_amount IS NOT NULL
  ));
```

This will add a `predicted_tip_amount` column to the output, showing the predicted tip for each taxi ride.

### 7. Explain Predictions

The `EXPLAIN_PREDICT` function can reveal which features had the most impact on the model's predictions.

The following query shows the top 3 contributing features:

```sql
-- PREDICT AND EXPLAIN
SELECT
  *
FROM
  ML.EXPLAIN_PREDICT(MODEL `taxi-rides-ny.nytaxi.tip_model`,
  (
    SELECT
      *
    FROM
      `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
      tip_amount IS NOT NULL
  ), STRUCT(3 as top_k_features));
```

This is particularly useful when you need to explain the model’s decision-making process or optimize it further.

### 8. Hyperparameter Tuning

BigQuery ML allows users to optimize the model’s performance through **hyperparameter tuning**. The following query demonstrates how to create a linear regression model with hyperparameter tuning, adjusting parameters like `l1_reg` and `l2_reg`:

```sql
-- HYPER PARAM TUNNING
CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_hyperparam_model`
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['tip_amount'],
  DATA_SPLIT_METHOD='AUTO_SPLIT',
  num_trials=5,
  max_parallel_trials=2,
  l1_reg=hparam_range(0, 20),
  l2_reg=hparam_candidates([0, 0.1, 1, 10])) AS
SELECT
  *
FROM
  `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
  tip_amount IS NOT NULL;
```

This query performs hyperparameter tuning by testing 5 different trials with a maximum of 2 parallel trials, exploring values for the `l1_reg` and `l2_reg` parameters.

Hyperparameter tuning ensures that the model achieves the best possible performance by testing different values for the regularization parameters.

## 📊 Evaluation Metrics

The most commonly used evaluation metrics for machine learning models are:

- **Mean Absolute Error (MAE)**: The average of the absolute differences between the predicted and actual values. A smaller MAE indicates a better fit.
- **Mean Squared Error (MSE)**: Measures the average of the squared differences between predicted and actual values. Larger errors are penalized more heavily.

## 📚 Additional Resources

- [The CREATE MODEL statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create)
- [Regression and Classification](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-glm)
