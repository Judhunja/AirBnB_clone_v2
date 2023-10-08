#!/usr/bin/env bash
# This script prepares my web servers to deploy using
# fabric
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

sudo echo "Finish all projects!" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

loc="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"

sudo sed -i "/server {/a $loc" /etc/nginx/sites-available/default

sudo service nginx restart
