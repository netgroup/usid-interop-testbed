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
