# Connecting pgAdmin and Postgres with Docker

## Overview

This session covers how to use [pgAdmin](https://www.pgadmin.org/) to interact with a **PostgreSQL** database running in **Docker**.

The goal here is to compare the ease of **pgAdmin** for database management compared to command-line tools, as well as the process of setting up both **PostgreSQL** and **pgAdmin** containers within the same **network** for seamless communication.

---

### Key Concepts and Steps

### 1. **Why Use pgAdmin**

- pgAdmin provides a convenient, graphical interface for writing and executing SQL queries.
- Unlike CLI tools like `pgcli`, pgAdmin allows you to view query results in a tabular format and manage databases more efficiently.

### 2. **Setting Up pgAdmin with Docker**

- Use Docker to avoid the need for direct installation.
- The official Docker image for pgAdmin can be found on Docker Hub.

### 3. **Create a Docker Network**

> [!IMPORTANT] Very Important
> **Challenge**: pgAdmin and PostgreSQL containers cannot communicate directly because `localhost` inside one container refers to itself, not another container.
>
> **Solution**: Use Docker networks to allow the containers to communicate.

#### 1. Create a Docker network

```bash
docker network create pg-network
```

#### 2. Run PostgreSQL in the same network

```bash
docker run -it \
    --name pg-database \
    --network=pg-network \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres:13
```

#### 3. Run pgAdmin in the same network

- `--network pg-network`: Assigns the container to the created network.
- `--name pg-database`: Gives the container a recognizable name for network-based communication.

- Run pgAdmin in the same network:

```bash
docker run -it \
    --name pg-admin \
    --network pg-network \
    -e PGADMIN_DEFAULT_EMAIL=admin@admin.com \
    -e PGADMIN_DEFAULT_PASSWORD=root \
    -p 8080:80 \
    -d dpage/pgadmin4
```

### 4. **Connecting pgAdmin to PostgreSQL**

- Access pgAdmin at `http://localhost:8080`.
- Login with the credentials provided in the `docker run` command.
- Add a new server:

  1. Right-click on "Servers" → Select "Register" → "Server".
  2. Under the "General" tab, provide a name (e.g., `docker_local`).
  3. In the "Connection" tab:
      - **Host**: Use the container name of the PostgreSQL instance (e.g., `pg-database`).
      - **Username**: `root`
      - **Password**: `root`
- Save the configuration to connect.

### 5. **Exploring the Database**

On the pgAdmin interface navigate to:

- Databases → ny_taxi → schemas → tables → yellow_taxi_data.
- Right click on the `yellow_taxi_data` and select `Query Tool`.
- Check the data:

  ```sql
  SELECT COUNT(*) FROM yellow_taxi_data;
  ```

  - This retrieves the total number of records in the table.

  ```sql
  SELECT * FROM yellow_taxi_data LIMIT 10;
  ```

  - This retrieves the first 10 records from the table.

---

### Key Takeaways

- Docker simplifies running tools like pgAdmin without direct installation.
- Networking is essential for inter-container communication in Docker.
- pgAdmin enhances the usability of PostgreSQL with its graphical interface and query tools.
- Use container names in custom networks to reference services easily.
