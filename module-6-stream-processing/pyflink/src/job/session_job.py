from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import EnvironmentSettings, DataTypes, TableEnvironment, StreamTableEnvironment
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.datastream.window import EventTimeSessionWindows
from pyflink.common.time import Duration
from pyflink.table.window import Session



source_table_name = "events"
sink_table_name = 'location_streaks'

def create_source_table(t_env, table_name):
    source_ddl = f"""
        CREATE TABLE {table_name} (
            lpep_pickup_datetime TIMESTAMP(3),
            lpep_dropoff_datetime TIMESTAMP(3),
            PULocationID INT,
            DOLocationID INT,
            passenger_count INT,
            trip_distance NUMERIC,
            tip_amount NUMERIC,
            WATERMARK for lpep_dropoff_datetime as lpep_dropoff_datetime - INTERVAL '5' SECOND
        ) WITH (
            'connector' = 'kafka',
            'properties.bootstrap.servers' = 'redpanda-1:29092',
            'topic' = 'green-trips',
            'scan.startup.mode' = 'earliest-offset',
            'properties.auto.offset.reset' = 'earliest',
            'format' = 'json'
        );
        """
    t_env.execute_sql(source_ddl)


def create_sink_table(t_env, table_name):
    sink_ddl = f"""
        CREATE OR REPLACE TABLE {table_name} (
            session_start TIMESTAMP(3),
            session_end TIMESTAMP(3),
            PULocationID INT,
            DOLocationID INT,
            streak_count BIGINT
        ) WITH (
            'connector' = 'jdbc',
            'url' = 'jdbc:postgresql://postgres:5432/postgres',
            'table-name' = '{table_name}',
            'username' = 'postgres',
            'password' = 'postgres',
            'driver' = 'org.postgresql.Driver'
        );
        """
    t_env.execute_sql(sink_ddl)


def run_job():
    # Set up the execution environment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.enable_checkpointing(10 * 1000)
    env.set_parallelism(1)

    # Set up the table environment
    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    t_env = StreamTableEnvironment.create(env, environment_settings=settings)

    try:
        # Create Kafka table
        create_source_table(t_env, source_table_name)
        create_sink_table(t_env, sink_table_name)

        t_env.execute_sql(
            f"""
                    INSERT INTO {sink_table_name}
                    SELECT
                        SESSION_START(lpep_dropoff_datetime, INTERVAL '5' MINUTES) as session_start,
                        SESSION_END(lpep_dropoff_datetime, INTERVAL '5' MINUTES) as session_end,
                        PULocationID,
                        DOLocationID,
                        COUNT(*) AS streak_count
                    FROM {source_table_name}
                    GROUP BY
                        PULocationID,
                        DOLocationID,
                        SESSION(lpep_dropoff_datetime, INTERVAL '5' MINUTE)
                    """
        ).wait()

    except Exception as e:
        print("Writing records from Kafka to JDBC failed:", str(e))


if __name__ == '__main__':
    run_job()
