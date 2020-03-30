#this will start a t2.micro w/ the amazon linux machine
# set up the provider first - configure our AWS account  
provider "aws" {
	access_key = "ACCESS_KEY"
	secret_key = "SECRET_KEY" 
	project = "project-id-name"
	region = "us-east-1"
}

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

# still need to add more parts to this for it to be more complete.

# -----------------------------------------------

# Security Group 

# -----------------------------------------------
resource "aws_security_group" "allow_all" {
	name = "allow_all"
	description = "Allow all inbound traffic"
	vpc_id = "${aws_vpc.main.id}"

	ingress {
		from_port = 0
		to_port = 0 
		protocol = "-1"
		cidr_blocks = ["0.0.0.0/0"]
	} 
}

#-------------------------------------------

# VPC 

#-----------------------------------------

resource "aws_vpc" "main" {
	cidr_block = "my.cidr.block/16"
	enable_dns_hostnames = true
}

resource "aws_subnet" "main" {
	vpc_id = "${aws_vpc.main.id}"
	vidr_block = "my.cidr.block/20"
	map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "gw" {
	vpc_id = "${aws_vpc.main.id}"

	route { 
		cidr_block = "0.0.0.0/0"
		gateway_id = "${aws_internet_gateway.gw.id}"
	}
}
# not sure about this below
resource "aws_main_route_table_association" "a" {
	vpc_id = "${aws_vpc.main.id}"
	route_table_id = "${aws_route_table.r.id}"
}
# then we'd run terraform init, terraform plan and terraform apply  
