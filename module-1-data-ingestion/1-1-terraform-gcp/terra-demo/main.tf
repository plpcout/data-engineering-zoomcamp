terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  project = "terraform-demo-449123"
  region  = "us-east1"
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-demo-449123-terra-bucket"
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
