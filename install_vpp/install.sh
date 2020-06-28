#!/bin/bash

git clone https://github.com/FDio/vpp

cd vpp 
sudo apt install dh-python
sudo make install-dep
sudo make install-ext-dep
sudo make pkg-deb
sudo dpkg -i build-root/*.deb
cd ..
mkdir vpp-deb
cp vpp/build-root/*.deb vpp-deb
sudo rm -r vpp
