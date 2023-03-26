#!/bin/bash

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt -y install g++
sudo apt install software-properties-common
sudo apt install python3

cat define_run.sh >> ~/.bashrc

exec bash