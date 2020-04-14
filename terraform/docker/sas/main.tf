# configure docker provider 
provider "docker" {
  host = "tcp://127.0.0.1:2376/"

  registry_auth {
    address = "docker.sas.com"
    config_file = "config-file-path.json"
  }

  registry_auth {
    address = "docker.sas.com" 
    config_file_content = "${var.plain_content_of_config_file}"
  }

  registry_auth {
    address  = "some_addy"
    username = "jabras"
    password = "password" # find way to pull this w/out committing it

}



# need to figure out way to authorize this and give it the files it needs
# create my container
resource "docker_container" "con_SAS" {
  image = "${docker.sas.com/anbise/sas-programming:latest}"
  name = "jabrazzy_sas"
  
}

resource "docker_image" "sas_image" {
  name = "sas-programming:latest"
}	
