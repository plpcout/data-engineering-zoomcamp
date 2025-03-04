import argparse

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

parser = argparse.ArgumentParser()

parser.add_argument('--input_green', required=True)
parser.add_argument('--input_yellow', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()


input_green = args.input_green
input_yellow = args.input_yellow
output = args.output

spark = SparkSession.builder \
    .appName('sparksql') \
    .getOrCreate()

df_green = spark.read.parquet(input_green)
df_yellow = spark.read.parquet(input_yellow)

df_green = df_green.withColumnsRenamed(
    {
        "lpep_pickup_datetime":"pickup_datetime",
        "lpep_dropoff_datetime":"dropoff_datetime",
    }
)
df_yellow = df_yellow.withColumnsRenamed(
    {
        "tpep_pickup_datetime":"pickup_datetime",
        "tpep_dropoff_datetime":"dropoff_datetime",
    }
)

common_columns = ['VendorID',
 'pickup_datetime',
 'dropoff_datetime',
 'store_and_fwd_flag',
 'RatecodeID',
 'PULocationID',
 'DOLocationID',
 'passenger_count',
 'trip_distance',
 'fare_amount',
 'extra',
 'mta_tax',
 'tip_amount',
 'tolls_amount',
 'improvement_surcharge',
 'total_amount',
 'payment_type',
 'congestion_surcharge']

df_green_sort = df_green \
    .select(common_columns) \
    .withColumn('service_type', F.lit('Green'))

df_yellow_sort = df_yellow \
    .select(common_columns) \
    .withColumn('service_type', F.lit('Yellow'))

df_trips_data = df_green_sort.unionAll(df_yellow_sort)

df_trips_data.createOrReplaceTempView('trips_data')

df_result = spark.sql(
    """
    SELECT
        -- Reveneue grouping
        PULocationID AS revenue_zone,
        date_trunc('month', pickup_datetime) AS revenue_month,
        service_type,

        -- Revenue calculation
        SUM(fare_amount) AS revenue_monthly_fare,
        SUM(extra) AS revenue_monthly_extra,
        SUM(mta_tax) AS revenue_monthly_mta_tax,
        SUM(tip_amount) AS revenue_monthly_tip_amount,
        SUM(tolls_amount) AS revenue_monthly_tolls_amount,
        SUM(improvement_surcharge) AS revenue_monthly_improvement_surcharge,
        SUM(total_amount) AS revenue_monthly_total_amount,
        SUM(congestion_surcharge) AS revenue_monthly_congestion_surcharge,

        -- Additional calculations
        AVG(passenger_count) AS avg_montly_passenger_count,
        AVG(trip_distance) AS avg_montly_trip_distance
    FROM
        trips_data
    GROUP BY
        1, 2, 3
    """
)

df_result.coalesce(1).write.parquet(output, mode='overwrite')
