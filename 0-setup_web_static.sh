#!/usr/bin/env bash
# scripts that creates all neccesary directories and files
# for deployment

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

echo "<html>
      <head>
            <title>Airclone Deployment</title>
      </head>
      <body>
            <p>This a random content<p>
      </body>
      </html>" | sudo tee /data/web_static/releases/test/index.html

# Create Symbolic link
sudo ln -fs /data/web_static/releases/test/  /data/web_static/current

# Change Owner
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content="location /hbnb_static {\n\talias /data/web_static/current/;\n}\n"
sudo sed -i '/server_name _;/a '"$config_content"'' /etc/nginx/sites-available/default

sudo service nginx restart
