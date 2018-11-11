#!/bin/bash

virtualenv --python=/bin/python3.6 venv
source venv/bin/activate

# TODO CUDA for gpu computing
# install desktop pytorch
pip3 install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-linux_x86_64.whl

pip install -r requirements.txt
