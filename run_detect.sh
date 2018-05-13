#!/bin/bash
mkdir log
NOW=$(date +"%Y-%m-%d-%H-%M-%S")
python -u /home/pi/Documents/washingmachine/detect.py | tee /home/pi/Documents/washingmachine/log/log-$NOW.txt 
