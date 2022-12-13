#!/bin/sh

yum install java-1.8.0-openjdk-devel tree git wget -y

echo "Starting Installation.."

echo "Changing Directory to /opt"
cd /opt/

echo "Downloading Packages.."
wget https://releases.jfrog.io/artifactory/bintray-artifactory/org/artifactory/oss/jfrog-artifactory-oss/7.21.5/jfrog-artifactory-oss-7.21.5-linux.tar.gz
tar -xvzf jfrog-artifactory-oss-7.21.5-linux.tar.gz

cd artifactory-oss-7.21.5
cd app/bin

echo "Starting Artifactory.."
./artifactory.sh start

sleep 30

echo "Checking Artifactory Status.."
./artifactory.sh status

sleep 30

echo "Login using http://IPAddress:8082 with admin/password"
