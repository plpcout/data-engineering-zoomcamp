# Getting Started with Kestra

## 📌 Overview

This section provides a quick overview of **Kestra**'s initial workflow, which integrates with a notification channel. In this case, we will use **Discord** as the notification channel.

## 📑 Quick Summary
- **Event-driven orchestration** with automated execution
- **YAML-based workflow definitions** for simple configuration
- **Extensive plugin ecosystem** for integrations
- **Works with all types of pipelines**
- **Quick setup with Docker**
- **Built-in visual topology editor**

## 🛠️ Prerequisites

Before getting started, ensure you have the following installed:

- [**Docker**](https://www.docker.com/) (for running Kestra)
- [**Python**](https://www.python.org/), for Python tasks. **(Optional)**
- [**Discord account**](https://discord.com/), for notifications. **(Optional)**

## 📁 Files used in this notebook
- Kestra **`discord_webhook`** flow [2-2-2-flow.yml](../flows/2-2-2-flow.yml)

## 🎓 Core Concepts

### What is a Flow?

A **flow** is the fundamental unit of work in Kestra, defined in **YAML** with three key components:

| Component   | Description           | Example                   |
| ----------- | --------------------- | ------------------------- |
| `id`        | Unique identifier     | `github-monitor`          |
| `namespace` | Environment scope     | `production`              |
| `tasks`     | Operations to execute | Python scripts, API calls |

#### Flow Structure Example

```yaml
id: getting-started
namespace: example
tasks:
  - id: hello_world
    type: io.kestra.core.tasks.log.Log
    message: "Hello World!"
```

### Flow Components

#### 📥 Inputs

Dynamic values configured at the flow level:

- Avoid hardcoding repeated values.
- Accessible throughout the flow.

```yaml
inputs:
  - id: variable_name
    type: STRING
    default: example_string
```

#### 📤 Outputs

Data produced by tasks:

- Can be used in subsequent tasks.
- Useful for passing files or variables between tasks.

```yaml
outputs:
  - id: result
    value: "{{ outputs.previous_task.data }}"
```

#### ⏰ Triggers

Automatically execute flows:

- **Types:**
  - Schedule-based (cron expressions)
  - Webhook-based
  - Custom conditions

```yaml
triggers:
  - id: hourly
    type: schedule
    cron: "0 * * * *"
```

---

## 💡 Implementation Example - GitHub Stars Monitor

A flow that checks **GitHub repository stars** and sends notifications to **Discord**.

> [!TIP]
>
> For this example, a **Discord Webhook** is required. If you need further information on how to set up a Discord webhook, check out [**Discord - Intro to Webhooks**](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).

### Quick Start

1. **Launch Kestra using Docker:**
   ```bash
   docker run \
     --pull=always \
     --rm \
     -it \
     -p 8080:8080 \
     --user=root \
     -v /var/run/docker.sock:/var/run/docker.sock \
     -v /tmp:/tmp \
     kestra/kestra:latest-full server local
   ```
2. **Access Kestra UI:** Open [localhost:8080](http://localhost:8080)

### Creating Files

1. **Create a  new Flow and navigate to its editor tab.**
2. **Create a `scripts/` folder.**
3. **Inside `scripts/`, create `api_example.py`**:

```python
import requests
from kestra import Kestra

# Fetch repository statistics
response = requests.get("https://api.github.com/repos/kestra-io/kestra")
gh_stars = response.json()["stargazers_count"]

# Send data back to Kestra
Kestra.outputs({"gh_stars": gh_stars})
```

4. **Inside `scripts/`, create `requirements.txt`**:

```txt
requests
kestra
```

5. **Define your Kestra flow:**

```yaml
id: github-stars-monitor
namespace: tutorial

inputs:
  - id: kestra_logo
    type: STRING
    default: https://avatars.githubusercontent.com/u/59033362?v=4
  - id: discord_webhook_url
    type: STRING
    # Change this to your Discord Webhook
    default: <DISCORD_WEBHOOK_URL>

tasks:
  - id: python_script
    type: io.kestra.plugin.scripts.python.Commands
    namespaceFiles:
      enabled: true
    beforeCommands:
      - python -m venv .venv
      - source .venv/bin/activate
      - pip install -r scripts/requirements.txt
    commands:
      - python ./scripts/api_example.py
    taskRunner:
      type: io.kestra.plugin.scripts.runner.docker.Docker

  - id: output_gh_stars
    type: io.kestra.plugin.core.log.Log
    message: "Number of stars: {{outputs.python_script.vars.gh_stars}}"

  - id: send_notification
    type: io.kestra.plugin.notifications.discord.DiscordExecution
    content: "Total of GitHub Stars: {{outputs.python_script.vars.gh_stars}}"
    username: Kestra
    avatarUrl: "{{inputs.kestra_logo}}"
    url: "{{inputs.discord_webhook_url}}"

triggers:
  - id: hourly_trigger
    type: io.kestra.plugin.core.trigger.Schedule
    # cron expression to every hour
    cron: "0 * * * *"
    # true - to disable the trigger
    disabled: false
```
> [!TIP]
>
> This can be done either by coding on the `source` tab or using the `topology` tab ui.

### Execution
   - Click `Execute` in **Kestra UI** and check the Logs tab.

   - Also, check your **Discord server** for the notification.

### 🎉 **Congratulations**! You've successfully implemented a GitHub Stars Monitor


## 🎯 Best Practices

### File Management

- Keep files **organized** by type.
- Use **meaningful file names**.
- Use **version control** (e.g., Git).

### Trigger Configuration

- **Design efficient triggers**.
- **Test trigger behavior**.
- **Monitor execution performance**.

> [!TIP]
> Use [**crontab.guru**](https://crontab.guru) to generate and validate cron expressions.

### Development Guidelines

- **Version control** all flows.
- **Thoroughly test** before deploying.
- **Monitor execution times**.
- **Implement error handling**.

### Organization

- Use **meaningful namespaces**.
- **Group related tasks**.
- Maintain **consistent naming conventions**.
- **Document flow purpose**.

## 📚 Additional Resources
 - [**Install Kestra with Docker Compose**](https://kestra.io/docs/installation/docker-compose)
 - [**Tutorial**](https://kestra.io/docs/getting-started/tutorial) - to schedule and orchestrate your first workflows.
 - [**What is an Orchestrator?**](https://kestra.io/blogs/2024-09-18-what-is-an-orchestrator)

---

| [HOME](../README.md) | [<< BACK](./2-2-1-notes.md) | [NEXT >>](./2-2-3-notes.md) |
| -------------------- | ----------------------- | --------------------------- |
