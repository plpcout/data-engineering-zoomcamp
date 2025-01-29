# Terraform Variables

## Overview

 This document covers the **use of variables in Terraform**, a key feature for enhancing flexibility, reusability, and maintainability of infrastructure code. We will define and use variables within Terraform files, as well as how they improve your workflow when creating and managing resources.

---
- [Key Concepts and Sections](#key-concepts-and-sections)
    - [1. What Are Terraform Variables?](#1-what-are-terraform-variables)
    - [2. Defining Variables](#2-defining-variables)
    - [3. Using Variables in Your Terraform Configuration](#3-using-variables-in-your-terraform-configuration)
    - [4. Setting Default and Required Variables](#4-setting-default-and-required-variables)
    - [5. Passing Variables via Command Line](#5-passing-variables-via-command-line)
    - [6. Managing Multiple Variables](#6-managing-multiple-variables)
    - [7. Example: Using Variables for Google Cloud Resources](#7-example-using-variables-for-google-cloud-resources)
        - [Declaring variables](#declaring-variables)
        - [Using variables in resources](#using-variables-in-resources)
    - [8. Advanced Variable Usage: Functions and File Loading](#8-advanced-variable-usage-functions-and-file-loading)
    - [9. Terraform Workflow with Variables](#9-terraform-workflow-with-variables)
- [Best Practices for Using Variables](#best-practices-for-using-variables)
- [Key Takeaways](#key-takeaways)
- [Further Reading and Resources](#further-reading-and-resources)

## Key Concepts and Sections

### 1. What Are Terraform Variables?

Variables in Terraform are used to make your infrastructure code more flexible and reusable. Instead of hardcoding values into your configuration files, you define variables and reference them wherever needed. This allows you to easily adjust configurations without touching the core logic.

---

### 2. Defining Variables

Variables are defined in a separate `.tf` file, typically `variables.tf`. Here’s the basic syntax for declaring variables:

```hcl
variable "variable_name" {
  description = "A brief description of the variable's purpose"
  default     = "Default value"
}
```

**Example:**

```hcl
variable "bq_dataset_name" {
  description = "My BigQuery data set name"
  default     = "demo_dataset"
}
```

- **Description**: A short explanation of what the variable represents.
- **Default**: An optional default value if none is provided during runtime.

---

### 3. Using Variables in Your Terraform Configuration

Once you've defined your variables, you can reference them inside your main configuration file (`main.tf`). This makes your code more adaptable and cleaner.

```hcl
resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}
```

- Here, `var.bq_dataset_name` dynamically fetches the value defined for that variable.

---

### 4. Setting Default and Required Variables

- **Default variables**: If a default value is provided, the variable becomes optional.
- **Required variables**: Variables without default values are required and must be set before running Terraform.

**Example:**

```hcl
variable "location" {
  description = "The region where resources will be created"
  default     = "us-west1"
}
```

If a variable does not have a default, Terraform will prompt for its value during execution.

---

### 5. Passing Variables via Command Line

You can override default values or set required variables directly from the command line:

```bash
terraform apply -var "location=eu-west1"
```

This approach is helpful when deploying infrastructure to different environments.

---

### 6. Managing Multiple Variables

When working on larger projects, it's common to organize variables in separate files. For instance, `variables.tf` for definitions and `terraform.tfvars` for values.

> [!NOTE]
> To know more on `terraform.tfvars`, check out [Terraform TFVars](https://www.terraform.io/docs/language/values/variables.html#tfvars-files)

---

### 7. Example: Using Variables for Google Cloud Resources

Here’s how to use variables for configuring Google Cloud resources:

#### Declaring variables

```hcl
variable "bq_dataset_name" {
  description = "Name of the BigQuery dataset"
  default     = "demo_dataset"
}

variable "region" {
  description = "Region for resources"
  default     = "US"
}

# Another way of authenticating to GCP
variable "credentials" {
  description = "Path to the Google Cloud credentials file"
  default     = "./keys/my-credentials.json"
}
```

#### Using variables

```hcl
provider "google" {
  project = var.project
  region  = var.region
}
```

```hcl
resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}
```

> [!TIP]
> By using these variables, you can easily switch between different environments (e.g., change the location from `US` to `EU`).

---

### 8. Advanced Variable Usage: Functions and File Loading

We can also use functions within variables, such as the `file()` function to load the contents of a file dynamically.
- eg. Authenticating to GCP this way.

    ```hcl
    variable "credentials" {
    description = "Path to credentials JSON"
    default     = "./keys/my-credentials.json"
    }

    provider "google" {
    credentials = file(var.credentials)
    }
    ```

This approach helps automate the loading of sensitive credentials in a secure way.

---

### 9. Terraform Workflow with Variables

- **Define**: Create your variables in `variables.tf`.
- **Preview**: Use `terraform plan` to see the changes.
- **Apply**: Run `terraform apply` to implement the changes using your variables.
- **Destroy**: Clean up resources with `terraform destroy`.

Using variables across your Terraform configuration ensures that your infrastructure is both reusable and scalable.

---

## Best Practices for Using Variables

- **Consistency**: Use variables for common parameters (e.g., project ID, region, storage class).
- **Descriptive Naming**: Name your variables clearly to indicate their purpose.
- **Documentation**: Always provide a description for each variable to improve clarity.
- **Environment-Specific Files**: Use different `.tfvars` files for managing variables per environment (development, production).

---

## Key Takeaways

- **Flexibility**: Variables make your Terraform code adaptable to different environments and use cases.
- **Maintainability**: Changes can be made in one place (e.g., `variables.tf`) instead of multiple places in the code.
- **Automation**: Use variables for automating configurations, especially with service credentials and cloud resource locations.

---

## Further Reading and Resources

- [Terraform Documentation](https://www.terraform.io/docs)
- [Terraform Variables](https://www.terraform.io/docs/language/values/variables.html)
- [Google Cloud Provider for Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs)

---

| [HOME](../README.md) | [<< BACK](./1-1-2-notes.md) |
| -------------------- | ----------------------- |
