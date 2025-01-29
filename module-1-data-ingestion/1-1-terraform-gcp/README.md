# Terraform & Google Cloud Platform (GCP)

## Overview

The instructions in this repository provide guides and resources for setting up and managing infrastructure using **[Terraform](https://www.terraform.io)**, focusing on **[Google Cloud Platform](https://cloud.google.com)** (GCP).

It covers key Terraform concepts, variable management, and best practices for infrastructure automation.

## Getting Started

### To begin

1. Ensure you have Terraform installed. [Terraform Install Guide](https://www.terraform.io/downloads).
2. Follow the material starting on [1.1.1](./public_notes/1-1-1-notes.md).

> [!IMPORTANT]
>
> - Check the [Summary](#summary), and click on the desired topic for a detailed note.
> - There's a [Navigation Menu](#navigation-menu) at the bottom for easy navigation.

## Summary

### 1. [Terraform Introduction](./public_notes/1-1-1-notes.md)

#### 1.1. Key Topics

- What is Terraform and why use it?
- Core Terraform concepts (Infrastructure-as-Code, Providers, and Resource Management).
- Essential Terraform commands (`init`, `plan`, `apply`, `destroy`).
- Advantages of using Terraform for infrastructure automation.

#### 1.2. Highlights

- **Simplicity**: Define infrastructure in human-readable configuration files.
- **Automation**: Avoid manual provisioning by codifying infrastructure.
- **Reproducibility**: Easily recreate environments with Terraform.

---

### 2. [Terraform Basics and Infrastructure Management](./public_notes/1-1-2-notes.md)

#### 2.1. Key Topics

- Installing Terraform and setting up Google Cloud Platform (GCP).
- Creating a Service Account and configuring authentication.
- Managing Google Cloud Storage (GCS) buckets with Terraform.
- Running essential Terraform commands to provision resources.

#### 2.2. Highlights

- **Step-by-Step Guide**: Set up GCP and authenticate Terraform securely.
- **Hands-on Examples**: Provision a GCS bucket using Terraform.
- **Best Practices**: Secure service account keys and use `.gitignore` for sensitive files.

---

### 3. [Terraform Variables](./public_notes/1-1-3-notes.md)

#### 3.1. Key Topics

- What are Terraform variables and why use them?
- Defining and using variables in Terraform configurations.
- Setting default and required variables.
- Passing variables via command-line arguments.
- Using `.tfvars` files for managing multiple environments.
- Advanced usage of variables with functions and file loading.

#### 3.2. Highlights

- **Flexibility**: Avoid hardcoding values by using variables.
- **Maintainability**: Manage infrastructure efficiently across different environments.
- **Automation**: Pass variables dynamically using CLI or configuration files.

---

## Navigation Menu

| **Notes**                                                        | **Description**                                                 |
|-----------------------------------------------------------------|---------------------------------------------------------------|
| [1. Terraform Introduction](./public_notes/1-1-1-notes.md)      | Overview of Terraform concepts and core commands.             |
| [2. Terraform Basics](./public_notes/1-1-2-notes.md)            | Setting up Terraform with GCP, creating resources.            |
| [3. Terraform Variables](./public_notes/1-1-3-notes.md)         | Managing variables for flexible infrastructure configurations. |

---

**[Back to the top](#terraform--google-cloud-platform-gcp)**
