#!/usr/bin/bash


# Activate the node-manager virtual environment
source /home/rose/.envs/node-mgr-venv/bin/activate

# Start the node-manager
node_manager --env-file /home/rose/workspace/rose-srv6-control-plane/control_plane/node-manager/node_manager/config/node_manager.env
