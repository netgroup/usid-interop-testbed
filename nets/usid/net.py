#!/usr/bin/python

import os

from argparse import ArgumentParser
import python_hosts
import shutil
from mininet.topo import Topo
from mininet.node import Host, OVSBridge
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
from mininet.link import Link
from mininet.log import setLogLevel

#BASEDIR = "/home/user/mytests/ospf3routers/nodeconf/"
BASEDIR = os.getcwd()+"/nodeconf/"
OUTPUT_PID_TABLE_FILE = "/tmp/pid_table_file.txt"

PRIVDIR = '/var/priv'

# Path of the file containing the entries (ip-hostname)
# to be added to /etc/hosts
ETC_HOSTS_FILE = './etc-hosts'

# Define whether to add Mininet nodes to /etc/hosts file or not
ADD_ETC_HOSTS = True

class BaseNode(Host):

    def __init__(self, name, *args, **kwargs):
        dirs = [PRIVDIR]
        Host.__init__(self, name, privateDirs=dirs, *args, **kwargs)
        self.dir = "/tmp/%s" % name
        self.nets = []
        if not os.path.exists(self.dir):
            os.makedirs(self.dir) 

    def config(self, **kwargs):
        # Init steps
        Host.config(self, **kwargs)
        # Iterate over the interfaces
        first = True
        for intf in self.intfs.values():
            # Remove any configured address
            self.cmd('ifconfig %s 0' %intf.name)
            # # For the first one, let's configure the mgmt address
            # if first:
            #   first = False
            #   self.cmd('ip a a %s dev %s' %(kwargs['mgmtip'], intf.name))
        #let's write the hostname in /var/mininet/hostname
        self.cmd("echo '" + self.name + "' > "+PRIVDIR+"/hostname")
        if os.path.isfile(BASEDIR+self.name+"/start.sh") :
            self.cmd('source %s' %BASEDIR+self.name+"/start.sh")
        if os.path.isfile(BASEDIR+self.name+"/ctrl.conf") :
            self.cmd('source %s' %BASEDIR+self.name+"/ctrl.conf")

    def cleanup(self):
        def remove_if_exists (filename):
            if os.path.exists(filename):
                os.remove(filename)

        Host.cleanup(self)
        # Rm dir
        if os.path.exists(self.dir):
            shutil.rmtree(self.dir)

        remove_if_exists(BASEDIR+self.name+"/zebra.pid")
        remove_if_exists(BASEDIR+self.name+"/zebra.log")
        remove_if_exists(BASEDIR+self.name+"/zebra.sock")
        remove_if_exists(BASEDIR+self.name+"/isis8d.pid")
        remove_if_exists(BASEDIR+self.name+"/isis8d.log")
        remove_if_exists(BASEDIR+self.name+"/isisd.log")
        remove_if_exists(BASEDIR+self.name+"/isisd.pid")

        remove_if_exists(OUTPUT_PID_TABLE_FILE)

        # if os.path.exists(BASEDIR+self.name+"/zebra.pid"):
        #     os.remove(BASEDIR+self.name+"/zebra.pid")

        # if os.path.exists(BASEDIR+self.name+"/zebra.log"):
        #     os.remove(BASEDIR+self.name+"/zebra.log")

        # if os.path.exists(BASEDIR+self.name+"/zebra.sock"):
        #     os.remove(BASEDIR+self.name+"/zebra.sock")

        # if os.path.exists(BASEDIR+self.name+"/ospfd.pid"):
        #     os.remove(BASEDIR+self.name+"/ospfd.pid")

        # if os.path.exists(BASEDIR+self.name+"/ospfd.log"):
        #     os.remove(BASEDIR+self.name+"/ospfd.log")

        # if os.path.exists(OUTPUT_PID_TABLE_FILE):
        #     os.remove(OUTPUT_PID_TABLE_FILE)


class Router(BaseNode):
    def __init__(self, name, *args, **kwargs):
        BaseNode.__init__(self, name, *args, **kwargs)


class Switch(OVSBridge):

    def __init__(self, name, *args, **kwargs):
        # dirs = [PRIVDIR]
        OVSBridge.__init__(self, name, *args, **kwargs)
        self.dir = "/tmp/%s" % name
        self.nets = []
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def config(self, **kwargs):
        # pylint: disable=arguments-differ

        # Init steps
        OVSBridge.config(self, **kwargs)
        # Iterate over the interfaces
        for intf in self.intfs.values():
            # Remove any configured address
            self.cmd('ifconfig %s 0' % intf.name)
            # # For the first one, let's configure the mgmt address
            # if first:
            #   first = False
            #   self.cmd('ip a a %s dev %s' %(kwargs['mgmtip'], intf.name))
        # let's write the hostname in /var/mininet/hostname
        self.cmd("echo '" + self.name + "' > "+PRIVDIR+"/hostname")
        if os.path.isfile(BASEDIR+self.name+"/start.sh"):
            self.cmd('source %s' % BASEDIR+self.name+"/start.sh")

# the add_link function creates a link and assigns the interface names
# as node1-node2 and node2-node1
def add_link (my_net, node1, node2):
    my_net.addLink(node1, node2, intfName1=node1.name+'-'+node2.name,
                       intfName2=node2.name+'-'+node1.name)

def create_topo(my_net):
    h11 = my_net.addHost(name='h11', cls=BaseNode, mac="1a:d4:2c:10:c3:0e")
    h12 = my_net.addHost(name='h12', cls=BaseNode, mac="da:5a:ac:99:36:1a")
    h13 = my_net.addHost(name='h13', cls=BaseNode, mac="72:23:e6:72:5c:c1")

    h31 = my_net.addHost(name='h31', cls=BaseNode, mac="9e:48:e5:e9:eb:c5")
    h32 = my_net.addHost(name='h32', cls=BaseNode, mac="0a:46:e7:d7:26:1e")
    h33 = my_net.addHost(name='h33', cls=BaseNode, mac="26:42:d3:96:be:4c")

    h51 = my_net.addHost(name='h51', cls=BaseNode, mac="ee:f2:1e:4d:48:ab")
    h52 = my_net.addHost(name='h52', cls=BaseNode, mac="ee:63:94:3f:36:e4")
    h53 = my_net.addHost(name='h53', cls=BaseNode, mac="ee:97:e5:5e:0b:d2")

    h81 = my_net.addHost(name='h81', cls=BaseNode, mac="06:83:41:94:b5:98")
    h82 = my_net.addHost(name='h82', cls=BaseNode, mac="72:30:b4:d8:c9:bd")
    h83 = my_net.addHost(name='h83', cls=BaseNode, mac="c2:bc:7a:4a:f7:a6")

    hdc1 = my_net.addHost(name='hdc1', cls=BaseNode, mac="be:99:4d:64:a5:ca")
    hdc2 = my_net.addHost(name='hdc2', cls=BaseNode, mac="ae:ce:2e:85:98:9d")
    hdc3 = my_net.addHost(name='hdc3', cls=BaseNode, mac="5e:69:e1:72:fc:ec")

    controller = my_net.addHost(name='controller', cls=BaseNode,
                                sshd=False, inNamespace=False)

    r1 = my_net.addHost(name='r1', cls=Router)
    r2 = my_net.addHost(name='r2', cls=Router)
    r3 = my_net.addHost(name='r3', cls=Router)
    vpp_1 = my_net.addHost(name='vpp_1', cls=Router)
    vpp_2 = my_net.addHost(name='vpp_2', cls=Router)
    p4_1 = my_net.addHost(name='p4_1', cls=Router)
    p4_2 = my_net.addHost(name='p4_2', cls=Router)
    vpp_3 = my_net.addHost(name='vpp_3', cls=Router)

    #note that if the interface names are not provided,
    #the order of adding link will determine the
    #naming of the interfaces (e.g. on r1: r1-eth0, r1-eth1, r1-eth2...)
    # it is possible to provide names as follows
    # Link(h1, r1, intfName1='h1-eth0', intfName2='r1-eth0')
    # the add_link function creates a link and assigns the interface names
    # as node1-node2 and node2-node1

    #hosts of r1
    add_link(my_net, h11,r1)
    add_link(my_net, h12,r1)
    add_link(my_net, h13,r1)
    #r1 - r2
    add_link(my_net, r1,r2)
    #datacenters of r2
    add_link(my_net, hdc1,r2)
    #r2 - r3
    add_link(my_net, r2,r3)
    #r2 - p4_1
    add_link(my_net, r2,p4_1)
    #hosts of r3
    add_link(my_net, h31,r3)
    add_link(my_net, h32,r3)
    add_link(my_net, h33,r3)
    #r3 - vpp_1
    add_link(my_net, r3,vpp_1)
    #vpp_1 - vpp_2
    add_link(my_net, vpp_1,vpp_2)
    #vpp_1 - p4_2
    add_link(my_net, vpp_1,p4_2)
    #hosts of vpp_2
    add_link(my_net, h51,vpp_2)
    add_link(my_net, h52,vpp_2)
    add_link(my_net, h53,vpp_2)
    #datacenters of vpp_2
    add_link(my_net, hdc3,vpp_2)
    #vpp_2 - p4_2
    add_link(my_net, vpp_2,p4_2)
    #p4_2 - p4_1
    add_link(my_net, p4_2,p4_1)
    #p4_2 - vpp_3
    add_link(my_net, p4_2,vpp_3)
    #p4_1 - vpp_3
    add_link(my_net, p4_1,vpp_3)
    #hosts of vpp_3
    add_link(my_net, h81,vpp_3)
    add_link(my_net, h82,vpp_3)
    add_link(my_net, h83,vpp_3)
    #datacenters of vpp_3
    add_link(my_net, hdc2,vpp_3)

    # Create the mgmt switch
    sw = my_net.addSwitch(name='sw', cls=Switch, dpid='1')
    # Create a link between mgmt switch and controller
    add_link(my_net, controller, sw)
    # Connect all the routers to the management network
    add_link(my_net, r1, sw)
    add_link(my_net, r2, sw)
    add_link(my_net, r3, sw)
    add_link(my_net, vpp_1, sw)
    add_link(my_net, vpp_2, sw)
    add_link(my_net, vpp_3, sw)
    add_link(my_net, p4_1, sw)
    add_link(my_net, p4_2, sw)

    r1.cmd("source " + BASEDIR+"r1/ip-link.conf")
    r2.cmd("source " + BASEDIR+"r2/ip-link.conf")
    r3.cmd("source " + BASEDIR+"r3/ip-link.conf")
    p4_1.cmd("source " + BASEDIR+"p4_1/ip-link.conf")
    p4_2.cmd("source " + BASEDIR+"p4_2/ip-link.conf")


def add_nodes_to_etc_hosts():
    # Get /etc/hosts
    etc_hosts = python_hosts.hosts.Hosts()
    # Import host-ip mapping defined in etc-hosts file
    count = etc_hosts.import_file(ETC_HOSTS_FILE)
    # Print results
    count = count['add_result']['ipv6_count'] + count['add_result']['ipv4_count']
    print('*** Added %s entries to /etc/hosts\n' % count)


def remove_nodes_from_etc_hosts(net):
    print('*** Removing entries from /etc/hosts\n')
    # Get /etc/hosts
    etc_hosts = python_hosts.hosts.Hosts()
    for host in net.hosts:
        # Remove all the nodes from /etc/hosts
        etc_hosts.remove_all_matching(name=str(host))
    # Write changes to /etc/hosts
    etc_hosts.write()


def stopAll():
    # Clean Mininet emulation environment
    os.system('sudo mn -c')
    # Kill all the started daemons
    os.system('sudo killall sshd zebra isisd simple_switch')
    os.system('sudo kill $(pidof vpp)')

def extractHostPid (dumpline):
    temp = dumpline[dumpline.find('pid=')+4:]
    return int(temp [:len(temp)-2])


    
def simpleTest():
    "Create and test a simple network"

    #topo = RoutersTopo()
    #net = Mininet(topo=topo, build=False, controller=None)
    net = Mininet(topo=None, build=False, controller=None)
    create_topo(net)

    net.build()
    net.start()


    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    #print "Testing network connectivity"
    #net.pingAll()

    with open(OUTPUT_PID_TABLE_FILE,"w") as file:
        for host in net.hosts:
            file.write("%s %d\n" % (host, extractHostPid( repr(host) )) )

    # Add Mininet nodes to /etc/hosts
    if ADD_ETC_HOSTS:
        add_nodes_to_etc_hosts()

    CLI( net ) 

    # Remove Mininet nodes from /etc/hosts
    if ADD_ETC_HOSTS:
        remove_nodes_from_etc_hosts(net)

    net.stop() 
    stopAll()


def parse_arguments():
    # Get parser
    parser = ArgumentParser(
        description='Emulation of a Mininet topology (8 routers running '
                    'IS-IS, 1 controller out-of-band'
    )
    parser.add_argument(
        '--no-etc-hosts', dest='add_etc_hosts',
        action='store_false', default=True,
        help='Define whether to add Mininet nodes to /etc/hosts file or not'
    )
    # Parse input parameters
    args = parser.parse_args()
    # Return the arguments
    return args



if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_arguments()
    # Define whether to add Mininet nodes to /etc/hosts file or not
    ADD_ETC_HOSTS = args.add_etc_hosts
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
