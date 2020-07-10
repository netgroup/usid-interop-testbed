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

After entering the ``srv6`` subsection, load the YAML file containing the nodes configuration:
```
controller-srv6> usid --nodes-file nodes.yml
```

The CLI will print a list of the available nodes.

Finally you can create a uSID policy with the following command:
```
controller-srv6-usid> policy --op add --lr-destination fd00:0:32::2 --rl-destination fd00:0:11::2 --nodes r1,vpp_1,p4_2,r3
```

For a detailed description of the arguments, use the ``help`` command:
``
controller-srv6-usid> help policy
``

To exit from the CLI, you can use the ``exit`` command:
```
controller-srv6-usid> exit
controller-srv6> exit
controller> exit
```
