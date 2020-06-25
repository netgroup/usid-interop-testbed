#!/bin/sh
set -e
curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py

sudo python2 get-pip.py

git clone https://github.com/nanomsg/nnpy.git
# top of tree won't install
cd nnpy
git checkout c7e718a5173447c85182dc45f99e2abcf9cd4065
sudo pip install cffi
sudo pip install .
sudo pip install ipaddr
cd ..
