# Installing Apache Spark (Optional)

## 📌 Overview

Apache Spark requires a proper installation and environment setup to function efficiently. This section is straightforward and needs a couple steps the get up and running with PySpark.

## 💻 Setup

1. Install JDK 17, spark and hadoop with [SDKMan](https://sdkman.io/):

    ```shell
    sdk i java 17.0.13-librca
    sdk i spark 3.5.3
    sdk i hadoop 3.3.6
    ```

2. Install dependencies from pyproject.toml and activate the virtualenv:

    ```shell
    uv sync && source .venv/bin/activate
    ```

## 📚 Additional Resources

### DTC Zoomcamp suggested installation guides

- [Linux](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/linux.md)
- [macOS](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/macos.md)
- [Windows](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/windows.md)
