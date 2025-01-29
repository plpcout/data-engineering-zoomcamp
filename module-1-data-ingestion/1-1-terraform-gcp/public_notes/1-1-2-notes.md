# Terraform Basics and Infrastructure Management (GCP)

## Overview
This guide introduces **Terraform**, an **Infrastructure-as-Code** (IaC) tool used to automate and manage cloud infrastructure. You will learn how to set up Terraform with **Google Cloud Platform (GCP)**, manage resources such as **Google Cloud Storage (GCS) buckets**, and follow best practices to ensure secure and efficient usage.

---

## 🔍 Table of Contents

- [Getting Started](#getting-started)
   - [Install Terraform:](#install-terraform)
   - [Choose a Cloud Provider (GCP)](#choose-a-cloud-provider-gcp)
   - [Create a Service Account](#create-a-service-account)
   - [Authenticate Terraform](#authenticate-terraform)
- [Hands On: Creating a GCS Bucket](#hands-on-creating-a-gcs-bucket)
   - [1. Terraform Configuration Files](#1-terraform-configuration-files)
   - [2. Define the GCS Bucket in `main.tf`](#2-define-the-gcs-bucket-in-maintf)
   - [3. Run Terraform Commands](#3-run-terraform-commands)
- [Best Practices](#best-practices)
   - [1. Security](#1-security)
   - [2. Documentation](#2-documentation)
   - [3. Version Control](#3-version-control)
- [Terraform Commands cheat sheet](#terraform-commands-cheat-sheet)
- [Additional Resources](#additional-resources)

---

## Getting Started

### Install Terraform:
   - If you don't have Terraform installed, you can follow the [official installation guide](https://learn.hashicorp.com/tutorials/terraform/install-cli) for your OS.

### Choose a Cloud Provider (GCP)

1. **Create a Google Cloud Platform (GCP) account** if you don’t have one:
   - Visit the [GCP Console](https://console.cloud.google.com/) and create an account.

2. **Set up a GCP project** where you’ll manage your resources:
   - Navigate to **IAM & Admin** > **Create a Project** in the GCP Console.

### Create a Service Account

A **Service Account** will allow Terraform to interact with GCP securely.

1. **Create the Service Account**:
   - In the GCP Console, navigate to **IAM & Admin** > **Service Accounts**.
   - Click **Create Service Account** and give it a meaningful name, such as `terraform-runner`.
   - Assign the necessary **permissions**:
     - **Storage Admin** (for managing GCS buckets)
     - **BigQuery Admin** (for managing datasets)
     - **Compute Admin** (optional for managing VMs)

      > [!IMPORTANT]
      > Outside this learning environment, you should **always** follow the **principle of least privilege**.
      >
      > Avoid granting unnecessary permissions.

2. **Generate Service Account Key**:
   - Download the **JSON key** file. This file contains sensitive credentials for Terraform.

### Authenticate Terraform

1. **Authenticate using the Service Account**:
   - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your service account key:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS=~/.keys/<KEY_NAME>.json
     ```

2. **(Optional) Authenticate with gcloud**:
   - You can use the `gcloud` CLI to authenticate as well:
     ```bash
     gcloud auth activate-service-account --key-file=<KEY_PATH>
     ```

      >[!TIP]
      > If you don't have gcloud installed, you can refer to [install the gcloud CLI](https://cloud.google.com/sdk/docs/install) documentation.

---

## Hands On: Creating a GCS Bucket

Follow these steps to create a GCS Bucket using Terraform.

### 1. Terraform Configuration Files

- **`main.tf`**: Contains the configuration for your infrastructure.
  Example to configure GCP provider:

  ```terraform
  terraform {
    required_providers {
      google = {
        source  = "hashicorp/google"
        version = "5.6.0"
      }
    }
  }

  provider "google" {
    project = "<PROJECT_ID>"
    region  = "us-central1"
  }
  ```

>[!TIP]
> Use `terraform fmt` to format your Terraform configuration files.

### 2. Define the GCS Bucket in `main.tf`

Inside your `main.tf` file, add the following configuration to define a Google Cloud Storage bucket:

```terraform
resource "google_storage_bucket" "demo_bucket" {
  name          = "unique-bucket-name"
  location      = "US"
  force_destroy = true

   lifecycle_rule {
    condition {
      age = 1 # days
    }
    action {
      # abort multipart uploads that are not completed within 1 day
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
```

### 3. Run Terraform Commands

1. **Initialize Terraform**:
   ```bash
   terraform init
   ```

2. **Preview the changes**:
   ```bash
   terraform plan
   ```

3. **Apply the changes**:
   ```bash
   terraform apply
   ```

4. **Destroy the created resources** (optional):
   ```bash
   terraform destroy
   ```

---

## Best Practices

### 1. Security
- **Use environment variables** to manage credentials, not hard-coded values in `.tf` files.
- Always **exclude sensitive files** like `terraform.tfstate` from version control by adding it to `.gitignore`.

### 2. Documentation
- Use **comments** to describe your Terraform configurations and actions.
- Refer to the [Terraform Google Provider Documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs) for advanced options.

### 3. Version Control
- Use a `.gitignore` file to exclude sensitive files such as `terraform.tfstate` and `.terraform/` directories.

-  Here is a quick terraform [.gitignore template](https://www.gitignore.io/api/terraform).

---

## Terraform Commands cheat sheet

| Command             | Description                                      |
|---------------------|--------------------------------------------------|
| `terraform init`     | Initializes Terraform in the working directory. |
| `terraform plan`     | Previews the infrastructure changes.           |
| `terraform apply`    | Applies changes to create/update resources.    |
| `terraform destroy`  | Removes the infrastructure resources.          |
| `terraform fmt`      | Formats Terraform code.                        |
| `terraform validate` | Validates Terraform code.                       |
| `terraform output`   | Displays the values of output variables.        |
| `terraform show`     | Displays the Terraform configuration in text.   |


## Additional Resources

- [Terraform Documentation](https://www.terraform.io/docs)
- [Google Cloud Documentation](https://cloud.google.com/docs)
