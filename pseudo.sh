#!/bin/sh
python3 -m pip install -r ./Pseudo_labels/requirements.txt --upgrade
python3 ./Pseudo_labels/run.py --config "config.json"