#!/bin/sh
yum install epel-release -y
yum install centos-release-scl -y
yum install rh-python36 -y
scl enable rh-python36 bash
yum install python3-pip python3-devel gcc -y
yum install gcc-c++ -y
pip3 install uwsgi flask -y

