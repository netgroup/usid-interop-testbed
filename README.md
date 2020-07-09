# Micro SID interoperability testbed featuring Linux kernel, VPP and P4 dataplanes

This repository hosts a testbed to test the features of Micro SID in an emulated network featuring Linux, VPP and P4 dataplanes. 

## Repository structure

The repo is structured as follows:

- *install_bmv2/* contains the scripts to install bmv2, the P4 dataplane, and all its dependencies;
- *install_vpp/* contains the scripts to install vpp and all its dependencies;
- *nets/usid/* contains the a python script describing the mininet topology;
- *nets/usid/nodeconf/* contains a folder for each mininet node with the configuration files needed to correctly setup the nodes.

## Dependencies

It is strongly recommended to download the already prepared VM, as described in https://netgroup.github.io/rose/rose-vm.html, as it has most of the dependencies installed. 

After downloading the VM, it is possible to install VPP and P4 bmv2 as follows:

```
  cd install_bmv2/
  bash install.sh
  cd ..
  cd install_vpp/
  bash install.sh
  cd ..
```
