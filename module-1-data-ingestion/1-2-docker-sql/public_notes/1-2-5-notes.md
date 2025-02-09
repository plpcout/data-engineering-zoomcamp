# Running PostgreSQL and pgAdmin with Docker Compose

## Overview

This guide demonstrates how to use [Docker Compose](https://docs.docker.com/compose/) to set up and run PostgreSQL and pgAdmin.

Docker Compose simplifies managing multiple related containers by defining configurations in a single YAML file, making it easier to set up local environments and manage dependencies.

## Key Concepts

### What is Docker Compose?

- **Docker Compose** is a tool that allows you to define and manage multi-container Docker applications using a single YAML configuration file.
- Containers in a Compose setup share the same network and can easily communicate with each other.

### Benefits of Docker Compose

- Centralized configuration for multiple containers.
- Reduced complexity compared to running containers with long `docker run` commands.
- Simplifies management of containerized applications during local development and integration testing.

## Configuration Highlights

### YAML File Structure

- **File name**: `docker-compose.yaml`
- **Main sections**:
  - **`version`**: Specifies the Compose file format version (optional).
  - **`services`**: Defines the containers to run.
  - **`volumes`** and **`ports`**: Used for mapping data and networking between the host and containers.
  - **`environment`**: Defines environment variables for containers.

### Example Setup for PostgreSQL and pgAdmin

> [!TIP]
> Why such a verbose `docker-compose.yaml` file?
>
> - **To provide additional context for those new to Docker Compose.**

```yaml
# docker-compose file for running PostgreSQL and pgAdmin
# This file is used to define and run multi-container Docker applications

services:
  # PostgreSQL container
  pg-database:
    # use the official PostgreSQL 13 image
    image: postgres:13

    # set environment variables for the container
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: root
      POSTGRES_DB: ny_taxi

    # mount a volume from the host machine to persist data
    volumes:
      # mount the ny_taxi_postgres_data directory from the host machine
      # to the /var/lib/postgresql/data directory in the container
      - ./ny_taxi_postgres_data:/var/lib/postgresql/data:rw

    # expose port 5432 from the container to the host machine
    ports:
      - "5432:5432"

  # pgAdmin container
  pg-admin:
    # use the official pgAdmin 4 image
    image: dpage/pgadmin4

    # set environment variables for the container
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: root

    # expose port 8080 from the container to the host machine
    ports:
      - "8080:80"

    # make sure the pgAdmin container only starts once the PostgreSQL
    # container is up and running
    depends_on:
      - pg-database
```

## Commands Cheat Sheet

- **Start services**:

- ```bash
  docker-compose up -d
  ```

  - Add `-d` to run in detached mode.

- **Stop services**:

  ```bash
  docker-compose down
  ```

- **View running containers**:

  ```bash
  docker ps
  ```

## Key Takeaways

- **Ease of Use**: Using Docker Compose eliminates the need for lengthy commands and manual network setups.
- **Networking**: Services defined in `docker-compose.yaml` automatically share the same network.
- **Volume Persistence**: Data can be persisted across container restarts by mapping host directories to container paths in `volumes`.
- **Detachment Mode**: Running services in detached mode allows you to reclaim the terminal for other tasks.

### Example Usage

After starting the services, you can access:

- PostgreSQL at `localhost:5432`
- pgAdmin at `http://localhost:8080`

---

| [HOME](../README.md) | [<< BACK](./1-2-4-notes.md) | [NEXT >>](./1-2-6-notes.md) |
| -------------------- | ---------------------------- | --------------------------- |
