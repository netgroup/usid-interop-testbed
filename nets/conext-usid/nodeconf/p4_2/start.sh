#!/bin/bash

BASE_DIR=nodeconf
NODE_NAME=p4_2
THRIFT_PORT=4002
FRR_PATH=/usr/lib/frr

sysctl -w net.ipv6.conf.all.forwarding=1

ROUTING="static"

if [ $ROUTING == "isis" ]; then
	echo "no service integrated-vtysh-config" >> /etc/frr/vtysh.conf
	chown frr:frrvty $BASE_DIR/$NODE_NAME

	$FRR_PATH/zebra -f $PWD/$BASE_DIR/$NODE_NAME/zebra.conf -d -z $PWD/$BASE_DIR/$NODE_NAME/zebra.sock -i $PWD/$BASE_DIR/$NODE_NAME/zebra.pid

	sleep 1

	$FRR_PATH/isisd -f $PWD/$BASE_DIR/$NODE_NAME/isisd.conf -d -z $PWD/$BASE_DIR/$NODE_NAME/zebra.sock -i $PWD/$BASE_DIR/$NODE_NAME/isisd.pid
else
	source $BASE_DIR/$NODE_NAME/ip-addr.conf

	sleep 1

	source $BASE_DIR/$NODE_NAME/ip-route.conf
fi

simple_switch --thrift-port $THRIFT_PORT -i 0@$NODE_NAME-vpp_1 -i 1@$NODE_NAME-vpp_2 -i 2@$NODE_NAME-p4_1 -i 3@$NODE_NAME-vpp_3 -i 4@$NODE_NAME-sw $PWD/$BASE_DIR/$NODE_NAME/bmv2.json &

#simple_switch_CLI --thrift-port $THRIFT_PORT < $BASEDIR/$NODE_NAME/commands.txt

