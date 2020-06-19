#!/bin/sh

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
source $THIS_DIR/common.sh

set -e
git clone -b 0.12.0 https://github.com/apache/thrift.git thrift-0.12.0
cd thrift-0.12.0
./bootstrap.sh
./configure --with-cpp=yes --with-c_glib=no --with-java=no --with-ruby=no --with-erlang=no --with-go=no --with-nodejs=no
make -j2 && sudo make install
cd lib/py
sudo python setup.py install
cd ../../..
