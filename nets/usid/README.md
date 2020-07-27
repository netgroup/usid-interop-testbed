# Run the experiments
## Deploy the emulated testbed

To deploy the mininet topology, trigger the following command:

```
sudo - E python net.py
```

After the network setup, the mininet CLI should appear. From that CLI it is possible to access a node terminal with:

```
mininet> gterm <nodeName>
```

## Insert micro SID policies with the controller

The controller is available at https://github.com/netgroup/rose-srv6-control-plane. For the installation instructions, see the README file and the documentation contained in the *rose-srv6-control-plane* repository.

We strongly recommend to use the ready-to-go VM available at https://netgroup.github.io/rose/rose-vm.html which already integrates the controller. If you use the VM, you don't need to manually setup the controller.

To start the controller, ``cd`` to the controller folder with the following command:

```
$ cd ~/workspace/rose-srv6-control-plane/control_plane/controller
```

And then start the controller with:
```
$ bash starter.sh
```

Now the controller CLI is ready to receive commands:
```
controller> 
```

To insert SID policies with the controller, enter the ``srv6`` subsection of the CLI:
```
controller> srv6
```

Then you can create a uSID policy with the following command:
```
controller(srv6)> policy --op add --lr-destination fd00:0:32::2 --rl-destination fd00:0:11::2 --nodes 0100,0200,0300 --l-grpc-ip fcfd:0:0:1::1 --l-grpc-port 12345 --l-fwd-engine Linux --r-grpc-ip fcfd:0:0:3::1 --r-grpc-port 12345 --r-fwd-engine Linux --decap-sid f00d --locator fcbb:bbbb::
```

The command requires the following arguments:
* *--op*,
      the operation to be performed (e.g. *add*, *get*, *change*, *del*).
* *--lr-destination*,
      the destination for the left-to-right path.
* *--rl-destination*,
      the destination for the right-to-left path.
* *--nodes*,
      the list of nodes for the left-to-right path. The nodes list support node names, uN SIDs (IPv6 addresses) and uSID identifiers. In order to use node names, you need to load the configuration of the nodes, as described below.
* *--nodes-rev* (optional),
      the SID list for the right-to-left path.  The nodes list support node names, uN SIDs (IPv6 addresses) and uSID identifiers. In order to use node names, you need to load the configuration of the nodes, as described below. If not provided, the reverse path will be symmetric.
* *--l-grpc-ip*,
      the gRPC address of the left endpoint of the path, required if the left node in the nodes list is expressed as uN SID or uSID identifier.
* *--l-grpc-port*,
      the gRPC port of the left endpoint of the path, required if the left node in the nodes list is expressed as uN SID or uSID identifier.
* *--l-fwd-engine*,
      the forwarding engine of the left endpoint of the path (e.g. *Linux* or *VPP*), required if the left node in the nodes list is expressed as uN SID or uSID identifier.
* *--r-grpc-ip*,
      the gRPC address of the right endpoint of the path, required if the right node in the nodes list is expressed as uN SID or uSID identifier.
* *--r-grpc-port*,
      the gRPC port of the right endpoint of the path, required if the right node in the nodes list is expressed as uN SID or uSID identifier.
* *--r-fwd-engine*,
      the forwarding engine of the right endpoint of the path (e.g. *Linux* or *VPP*), required if the right node in the nodes list is expressed as uN SID or uSID identifier.
* *--decap-sid* (optional),
      the uDT SID to be used for decapsulation (e.g. *f00d*), required if the left node or the right node is expressed uSID identifier.
* *--locator*,
      the locator block (uSID block) to be used for the uSIDs (e.g. *fcbb:bbbb::*), required if the left node or the right node is expressed uSID identifier.

For a detailed description of the arguments, use the ``help`` command:
```
controller(srv6)> help usid_policy
```

The controller keeps track of the policy created on a database. You can use the following command to see the policy installed:
```
controller(srv6)> usid_policy --op get
```

For each policy, the ``get`` command will show an ID. The policy ID can be used to remove the policy:
```
controller(srv6)> usid_policy --op del --id 1000
```

To exit from the CLI, you can use the ``exit`` command:
```
controller(srv6)> exit
controller> exit
```

The command presented above require a large number of arguments. In order to simplify the setup of the policies, you can prepare a YAML file containing the configuration of the nodes (gRPC address, gRPC port, uN SID, uDT SID, forwarding engine).

The file *nodes.yaml* in the folder *conext-testbed/nets/usid/nodeconf/controller* contains the configuration for the nodes of this testbed.

To load the configuration, enter the ``topology`` section of the cli:
```
controller> topology
controller(topology)>
```

Then you can load the configuration file with the following command:
```
controller(topology)> load-nodes --nodes-file conext-testbed/nets/usid/nodeconf/controller/nodes.yaml
```

After loading the configuration you can create a policy providing the node names instead of using the uN SID or the uSID identifier.
```
controller(srv6)> usid_policy --op add --lr-destination fd00:0:32::2 --rl-destination fd00:0:11::2 --nodes r1,r2,r3
```

You can also combine node names, uN SIDs and uSID identifiers in the nodes list:
```
controller(srv6)> usid_policy --op add --lr-destination fd00:0:32::2 --rl-destination fd00:0:11::2 --nodes r1,0002,fcbb:bbbb:0003:: --r-grpc-ip fcfd:0:0:3::1 --r-grpc-port 12345 --r-fwd-engine Linux --decap-sid f00d --locator fcbb:bbbb::
```
