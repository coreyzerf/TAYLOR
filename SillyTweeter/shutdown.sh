#!/bin/bash
clear
echo "Shut down initiated."
/home/pi/SillyTweeter/SillyTweeter.py "Goodnight."
/home/pi/speech.sh "Goodnight."
sudo halt -h
