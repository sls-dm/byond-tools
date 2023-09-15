#!/bin/bash

echo MAKE SURE YOU RUN THIS COMMAND AS SUDO
sudo apt-get update
sudo apt-get upgrade
sudo dpkg --add-architecture i386
sudo apt update
sudo apt upgrade
sudo apt install python3 wget git unzip make sudo
sudo python3 INSTALL.py 515 1614