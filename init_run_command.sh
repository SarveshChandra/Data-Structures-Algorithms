#!/bin/bash

apt update
apt -y install g++
cat define_run.sh >> /root/.bashrc
exec bash