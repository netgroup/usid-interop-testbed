#!/bin/bash
set -e
sudo apt-get install -y \
    automake \
    cmake \
    libjudy-dev \
    libgmp-dev \
    libpcap-dev \
    libboost-dev \
    libboost-test-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    libboost-thread-dev \
    libevent-dev \
    libtool \
    flex \
    bison \
    pkg-config \
    g++ \
    libffi-dev \
    wget

tmpdir=`mktemp -d -p .`
cd $tmpdir

bash ../travis/install-thrift.sh
bash ../travis/install-nanomsg.sh
sudo ldconfig
bash ../travis/install-nnpy.sh

cd ..
sudo rm -rf $tmpdir

git clone https://github.com/p4lang/behavioral-model.git
cd behavioral-model
./autogen.sh
./configure
make -j2
sudo make install
cd ..
sudo rm -r behavioral-model
