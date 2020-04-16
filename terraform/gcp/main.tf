// configure the gcp provider
provider "google" {
  credentials = file{"CREDENTIALS_FIEL.json"}
  project     = "tf-app-prac"
  region      = "us-east1"
}

// provision engine vm- create random id for instance  
resource "random_id" "instance_id" {
  byte_length = 8 
}

// create a single gce instance 
resource "google_compute_instance" "default" {
  name         = "tf-app-vm-${random_id.instance_id.hex}"
  machine_type = "f1-micro"
  zone         = "us-east1-1"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  // install flask on all new instances 
  metatdata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python-pip rsync; pip install flask"
  
  network_interface {
    network = "default"
 
    access_config {
      // include this seciton to give the vm an external ip address 
    }
  
  metadata = {
    ssh-keys = "INSERT_USERNAME:${file("~/.ssh/id_rsa.pub")}"
  }
  }
}

resource "google_compute_firewall" "default" {
  name    = "flask-app-firewall"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["5000"]
  }
}    
