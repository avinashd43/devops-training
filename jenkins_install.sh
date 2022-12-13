#!/bin/sh

yum install java-1.8.0-openjdk-devel tree git wget -y

echo "Installing GIT Client..."
sudo yum install git -y
sleep 10

echo "Installing Maven..."
sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo --no-check-certificate
sudo yum install apache-maven -y
sleep 10

echo "Installing Jenkins..."
curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo
rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
yum install jenkins-2.332.1-1.1.noarch -y
systemctl daemon-reload
systemctl restart jenkins
sleep 30
systemctl status jenkins
systemctl enable jenkins
usermod --shell /bin/bash jenkins
echo "jenkins  ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers
echo "Access Jenkins http://IPAddress:8080/ with user name admin and password from /var/lib/jenkins/secrets/initialAdminPassword"
