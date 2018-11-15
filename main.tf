provider "aws" {
  region = "eu-central-1"
  # credentials needs to be inserted here
}


resource "aws_security_group" "allow_all" {
  name        = "allow_all"
  description = "Allow all inbound traffic"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}


data "aws_ami" "ubuntu" {
  most_recent = "true"

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDqBp0+VFYorU/BwEsoxEMPwB5xbWXWBu653TYqSSdjbi9b3UQKkt54WDKTZzm4so7p7RQ4vcEI5Z6FlJj/BtyWflHhe3cj3pJGsZqMWMKQMWwmjTR5WyCj9nf3o7oP0gwUyv877SrCz8I+b0BmfrGVldbQTeEcA/M82hh4ki88y9U4zd5gOkMuCM/u8MxgjvvsaIMGPEG56tvhfvFlp2j6uI92/cITJqZQzp/bSsmBohef373xfVbVfzkYpgeJ3+HFfgmcCdnthSye00ktOXFDYatwOfAu456w/b5gfptMgHhqNknd0jMleF4sWNKmEXLmwFB5i4+JuU6CN88y+Fzt"
}

resource "aws_instance" "inowas" {
    count                       = "6"
    ami                         = "${data.aws_ami.ubuntu.id}"
    instance_type               = "m4.xlarge"
    vpc_security_group_ids      = ["${aws_security_group.allow_all.id}"]
    associate_public_ip_address = true
    key_name                    = "${aws_key_pair.deployer.key_name}"
    tags {
        Name         = "APP-inowas"
    }
}