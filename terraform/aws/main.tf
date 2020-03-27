# this will start a t2.micro w/ the amazon linux machine
resource "aws_instance" "practice_instance" {
	ami = "ami-0c55b159cbfafe1f0"
	instance_type = "t2.micro"
	vpc_security_group_ids = [aws_security_group.instance.id]

	# some script we want it to run 
	user_data = <<-EOF
	#!/bin/bash
	echo "Hello, World" > index.html
	nohup busybox httpd -f -p 8080 & 
	EOF

	# we want to name our instance 
	tags = {
		Name = "terraform-prac"
	}
	
	lifecycle {
		create_before_destroy = true
	}
}

# link to my account 
provider "aws" { 
	credentials = "${file("account.json")}"
	project = "project-id-name"
	region = "us-east-1"
}
# still need to add more parts to this for it to be more complete. 
# then we'd run terraform init, terraform plan and terraform apply  
