# Docker Intro

## Overview

This guide provides step-by-step instructions for coding. The focus is on understanding and using Docker as a data engineer, including running PostgreSQL and creating your first data pipeline.

---

## Prerequisites

1. Install Docker on your machine. [Get Docker here](https://www.docker.com/).
2. Familiarity with basic terminal commands.
3. Visual Studio Code (recommended) or any code editor of your choice.

---

## Steps

### 1. **Introduction to Docker**

Docker is a tool that delivers software in packages called containers. Containers are isolated environments that ensure reproducibility and prevent conflicts.

**Why Docker?**

- Containers isolate dependencies and applications.
- Simplifies local experiments and integration testing.
- Provides reproducibility across different environments (e.g., local machine, cloud).

---

### 2. **Testing Docker Installation**

Run the following commands to verify Docker is installed correctly:

```bash
docker run hello-world
```

This will:

- Download the `hello-world` image from Docker Hub.
- Run the image to output a test message.

Run a basic Ubuntu container:

```bash
docker run -it ubuntu bash
```

- `-it` makes the container interactive.
- `bash` starts a Bash shell in the container.

Try commands like `ls` or `echo "Hello from Docker"`.

---

### 3. **Working with Docker Images**

#### a. Running a Python Container

Run a Python container interactively:

```bash
docker run -it python:3.12-slim bash
```

- This starts a Bash shell in a Python 3.12-slim container.
- Run Python commands by typing `python`.

Example:

```python
print("Hello, World!")
```

Exit the container with `Ctrl+D`.

#### b. Installing Dependencies in a Container

1. Start the container:

```bash
docker run -it python:3.12-slim bash
```

2. Install a library (e.g., pandas):

```bash
pip install pandas
```

3. Test the library:

```bash
python
import pandas as pd
print(pd.__version__)
```

Exit with `Ctrl+D`.

**Note:** Changes in a container are not persistent. Restarting the container will lose the installed library.

---

### 4. **Creating a Dockerfile**

A `Dockerfile` is used to create a custom Docker image.

#### a. Create a New Directory

```bash
mkdir intro
cd intro
```

#### b. Create a `Dockerfile`

```bash
touch Dockerfile
```

#### c. Add the Following to Your `Dockerfile`:

```Dockerfile
FROM python:3.12-slim
RUN pip install pandas
ENTRYPOINT ["bash"]
```

- `FROM` specifies the base image (Python 3.12-slim).
- `RUN` installs pandas.
- `ENTRYPOINT` sets the default command to Bash.

#### d. Build the Docker Image

Run the following command to build the image:

```bash
docker build -t python-pandas .
```

- `-t` tags the image with a name (`python-pandas`).
- `.` specifies the current directory.

#### e. Run the Custom Image

```bash
docker run -it python-pandas
```

- `-i` makes the container interactive.

Check python version:

```bash
python --version
```

Test pandas installation:

```bash
python
import pandas as pd
print(pd.__version__)
```

---

### 5. **Creating a Simple Data Pipeline**

#### a. Create a Python Script

Create a file `pipeline.py` in the same directory:

```python
import pandas as pd

# Placeholder for data processing
print("Pipeline execution started...")
print("Job finished successfully.")
```

#### b. Update the `Dockerfile`

Modify the `Dockerfile` to include the script:

```Dockerfile
FROM python:3.12-slim

RUN pip install pandas

WORKDIR /app

COPY pipeline.py pipeline.py

ENTRYPOINT ["bash"]
```

- `COPY` adds the script to the container.
- `ENTRYPOINT` Sets the default entrypoint command. In this case: `bash`.

#### c. Rebuild the Image

Rebuild the image to include the updated Dockerfile:

```bash
docker build -t pipeline .
```

#### d. Run the Data Pipeline

```bash
docker run pipeline
```

Expected output:

```bash
Pipeline execution started...
Job finished successfully.
```

### **6. Creating a Simple Data Pipeline with Args**

#### a. Create another Python Script

Create a file `pipeline-args.py` in the same directory:

```python
import sys
import pandas as pd

print(sys.argv)
day = sys.argv[1]
print(f"Pipeline execution finished for day: {day}")

```

#### b. Update the modified `Dockerfile`

Modify the `Dockerfile` to include the script:

```Dockerfile
FROM python:3.12-slim

RUN pip install pandas

WORKDIR /app

# COPY pipeline.py pipeline.py
COPY pipeline_args.py pipeline_args.py

# ENTRYPOINT ["bash"]
ENTRYPOINT ["python", "pipeline_args.py"]
```

- `ENTRYPOINT` Sets the default entrypoint command. In this case: `python pypeline_args.py`.

#### c. Rebuild the modified Image

Rebuild the image to include the updated Dockerfile:

```bash
docker build -t pipeline .
```

#### d. Run the new Data Pipeline

```bash
docker run pipeline 2025-18-01
```

Expected output:

```bash
['pipeline_args.py', '2025-18-01']
Pipeline execution finished for day: 2025-18-01
```

---

### 7. Extra

#### a. If you want to delete a single instance

- Conteiner: `docker rm container_name|container_id`

- Image: `docker rmi image_name|image_id`

#### b. If you want to delete all instances

If you want to clear your docker environment, you can delete all containers and images.

**Warning:** This will remove **ALL** containers and images.

- Delete all containers:

```bash
docker rm $(docker ps -a -q)
```

- Delete all images:

```bash
docker rmi $(docker images -q)
```
