#!/usr/bin/bash


# Activate the controller virtual environment
source /home/rose/.envs/controller-venv/bin/activate

# Start the controller
controller --env-file /home/rose/workspace/rose-srv6-control-plane/control_plane/controller/controller/config/controller.env
