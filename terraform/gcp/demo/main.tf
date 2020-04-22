provider "google" {
  version = "~> 1.7"
  project = "jbrazzy-terraform"
  region  = "us-east1"
}

resource "google_compute_disk" "default" {
  count = 2
  name = "test-image-${count.index}"
  type = "pd-ssd"
  image = "debian-8-jessie-v20170523"
  zone = "us-east1-a"

# what does this do? 
  provisioner "local-exec" {
    command = "echo disk ${count.index}: ${self.self_link} >> disk_urls.txt"
  }
}

