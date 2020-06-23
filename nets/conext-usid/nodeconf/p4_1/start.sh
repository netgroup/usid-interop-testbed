#!/bin/bash

BASE_DIR=nodeconf
NODE_NAME=p4_1
THRIFT_PORT=4001
FRR_PATH=/usr/lib/frr

source $BASE_DIR/$NODE_NAME/ip-addr.conf

sleep 1

source $BASE_DIR/$NODE_NAME/ip-route.conf

simple_switch --thrift-port $THRIFT_PORT -i 0@$NODE_NAME-r2 -i 1@$NODE_NAME-p4_2 -i 2@$NODE_NAME-vpp_3 -i 3@$NODE_NAME-sw $PWD/$BASE_DIR/$NODE_NAME/bmv2.json &

# simple_switch_CLI --thrift-port $THRIFT_PORT < $PWD/$BASE_DIR/$NODE_NAME/commands.txt
