# Module 5 Homework

In this homework we'll put what we learned about Spark in practice.

For this homework we will be using the Yellow 2024-10 data from the official website:

```bash
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-10.parquet
```

## Question 1: Install Spark and PySpark

- Install Spark
- Run PySpark
- Create a local spark session
- Execute spark.version.

What's the output?

> [!NOTE]
> To install PySpark follow this [guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/pyspark.md)

<details>
<summary>Solution</summary>
<br>

![alt text](../assets/hw/images/image-1.png)

### Answer

spark.version = '3.5.3'

<br>
</details>

## Question 2: Yellow October 2024

Read the October 2024 Yellow into a Spark Dataframe.

Repartition the Dataframe to 4 partitions and save it to parquet.

What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.

- 6MB
- 25MB
- 75MB
- 100MB

<details>
<summary>Solution</summary>
<br>

![alt text](../assets/hw/images/image-2.png)

### Answer

- [ ] 6MB
- [x] 25MB
- [ ] 75MB
- [ ] 100MB

<br>
</details>

## Question 3: Count records

How many taxi trips were there on the 15th of October?

Consider only trips that started on the 15th of October.

- 85,567
- 105,567
- 125,567
- 145,567

<details>
<summary>Solution</summary>
<br>

I would like to understand, "What exactly is a taxi trip?"

eg. Should we consider:

- `trip duration` > 0
- `trip distance` > 0
- `total_amount` > 0
- `passenger_count` > 0
- `VendorID` not null
- `PULocationID` not null
- `DOLocationID` not null

Those might drastically change the result.
However, considering only the trips starting date as suggested by the question:

- `tpep_pickup_datetime` = '2024-10-15'

![alt text](../assets/hw/images/image-3.png)

### Answer

- [ ] 85,567
- [ ] 105,567
- [x] 125,567
- [ ] 145,567

<br>
</details>

## Question 4: Longest trip

What is the length of the longest trip in the dataset in hours?

- 122
- 142
- 162
- 182

<details>
<summary>Solution</summary>
<br>

![alt text](../assets/hw/images/image-4.png)

### Answer

- [ ] 122
- [ ] 142
- [x] 162
- [ ] 182

<br>
</details>

## Question 5: User Interface

Spark’s User Interface which shows the application's dashboard runs on which local port?

- 80
- 443
- 4040
- 8080

<details>
<summary>Solution</summary>
<br>

![alt text](../assets/hw/images/image-5.png)

### Answer

- [ ] 80
- [ ] 443
- [x] 4040
- [ ] 8080

<br>
</details>

## Question 6: Least frequent pickup location zone

Load the zone lookup data into a temp view in Spark:

```bash
wget https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
```

Using the zone lookup data and the Yellow October 2024 data, what is the name of the LEAST frequent pickup location Zone?

- Governor's Island/Ellis Island/Liberty Island
- Arden Heights
- Rikers Island
- Jamaica Bay

<details>
<summary>Solution</summary>
<br>

![alt text](../assets/hw/images/image-6.png)
### Answer

- [x] Governor's Island/Ellis Island/Liberty Island
- [ ] Arden Heights
- [ ] Rikers Island
- [ ] Jamaica Bay

<br>
</details>

## Submitting the solutions

- Form for submitting: <https://courses.datatalks.club/de-zoomcamp-2025/homework/hw5>
- Deadline: See the website
