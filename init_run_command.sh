#!/bin/bash

add-apt-repository ppa:deadsnakes/ppa
apt update
apt -y install g++
apt install software-properties-common
apt install python3.8

cat define_run.sh >> /root/.bashrc

exec bash