# BigQuery Machine Learning Model Deployment

## 📌 Overview

BigQuery ML allows users to train and deploy machine learning models directly within Google BigQuery. Once a model is trained, it can be exported and deployed for inference.

Deploying a machine learning model trained in BigQuery involves:

- Exporting the model
- Setting up a serving directory
- Running a model-serving Docker container to handle inference requests
  - (such as **TensorFlow Serving**, **TorchServe**, or others)

## 🛠️ Prerequisites

This is a hands-on approach to deploy a machine learning model.
To replicate, make sure you have:

- Docker installed on the local system

- Postman or `curl` for making HTTP requests
- Google Cloud SDK (`gcloud`) installed and authenticated

## ⚙️ Steps for Deployment

### 1. Authenticate with Google Cloud

Ensure authentication is completed using:

```sh
gcloud auth login
```

### 2. Export the Model to Google Cloud Storage

Run the following command to export the model:

```sh
bq --project_id taxi-rides-ny \
   extract -m nytaxi.tip_model \
   gs://taxi_ml_model/tip_model
```

🔹 _Verify that the exported model appears in the specified bucket._

### 3. Copy the Model to a Local Directory

Create a local directory and copy the model files:

```sh
mkdir /tmp/model

# Copy the model from Google Cloud Storage
gsutil cp -r gs://taxi_ml_model/tip_model /tmp/model
```

### 4. Set Up a Serving Directory

Create a directory for serving the model and move the exported model into it:

```sh
mkdir -p serving_dir/tip_model/1

# Copy model files to the serving directory
cp -r /tmp/model/tip_model/* serving_dir/tip_model/1
```

### 5. Pull the TensorFlow Serving Docker Image

Fetch the latest TensorFlow Serving image:

```sh
docker pull tensorflow/serving
```

### 6. Run the TensorFlow Serving Container

Start a Docker container with TensorFlow Serving:

```sh
docker run -p 8501:8501 \
   --mount type=bind,source=$(pwd)/serving_dir/tip_model,target=/models/tip_model \
   -e MODEL_NAME=tip_model \
   -t tensorflow/serving &
```

### 7. Verify the Deployment

Check if the container is running:

```sh
docker ps
```

### 8. Send API Requests

Use Postman or `curl` to interact with the model.

#### Check Model Version

```sh
curl -X GET http://localhost:8501/v1/models/tip_model
```

#### Make a Prediction Request

Send a POST request with input parameters:

```sh
curl -d '{
   "instances": [
      {
         "passenger_count": 1,
         "trip_distance": 12.2,
         "PULocationID": "193",
         "DOLocationID": "264",
         "payment_type": "2",
         "fare_amount": 20.4,
         "tolls_amount": 0.0
      }
   ]
}' \
-X POST http://localhost:8501/v1/models/tip_model:predict
```

Response should be similar to:

```json
{
  "predictions": [
    [
      3.2312432525242432
    ]
  ]
}
```

#### Interpret the Prediction

The response includes a predicted tip amount, which varies based on input parameters. Modifying the `payment_type` may significantly change the predicted amount.

## 📚 Additional Resources

- [BigQuery ML Model Deployment Tutorial](https://cloud.google.com/bigquery-ml/docs/export-model-tutorial)
