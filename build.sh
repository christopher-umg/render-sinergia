#!/usr/bin/env bash
# exit on error
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get -y install msodbcsql17

set -o errexit

python manage.py collectstatic --no-input
# python manage.py migrate