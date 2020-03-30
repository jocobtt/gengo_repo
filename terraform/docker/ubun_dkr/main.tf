# configure docker provider 
provider "docker" {
	host = "tcp://127.0.0.1:8080/"
}

# create a container 
resource "docker_container" "practice_container" {
	image = "${docker_image.ubuntu.latest}"
	name = "practice_container"
}

resource "docker_image" "ubuntu" {
	name = "ubuntu:latest"
}
