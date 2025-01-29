variable "project" {
  description = "My project"
  default     = "terraform-demo-449123"
}
variable "location" {
  description = "Project Location"
  default     = "us-west1"
}

variable "region" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery data set name"
  default     = "demo_dataset"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "terraform-demo-449123-terra-bucket"
}
