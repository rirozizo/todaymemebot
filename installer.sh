#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi
echo "Make sure all files are located in /home/pi/todaymemebot/ (including this installer)"
echo "Put your own API Key, API Secret, Access Token, and Access Token Secret inside driver.py"
echo "Adding tweepy to Python"
pip3 install tweepy
echo "Creating dummy jpg file so the script works (Don't delete!)"
touch local_image.jpg
echo "Modifying crontab to run at noon"
echo "0 12 * * * /usr/bin/python3 /home/pi/todaymemebot/driver.py > /home/pi/todaymemebot/log" >> /var/spool/cron/crontabs/root
echo "Done! use \"sudo crontab -e\" to edit when you want the script to tweet."
