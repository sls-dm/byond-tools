#!/bin/bash

echo "Fetching newest version..."
git clone https://github.com/slsgaming-net/byond-tools
echo "Successfully cloned byond-tools"
cd byond-tools
sudo sh run.sh