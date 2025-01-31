#!/bin/bash
set -e

echo "Deployment started ..."

# Pull the latest version of the app
echo "Copying New changes...."
git pull origin master
echo "New changes copied to server found!"

# Activate Virtual Env
#Syntax:- source virtual_env_name/bin/activate
source env/bin/activate
echo "Virtual env 'env' Activated !"


echo "Installing Dependencies..."
pip install -r requirements.txt --no-input

# echo "Clearing Cache..."
# python manage.py clean_pyc
# python manage.py clear_cache

echo "Serving Static Files..."
python manage.py collectstatic --noinput

echo "Running Database migration..."
python manage.py makemigrations
python manage.py migrate

# Deactivate Virtual Env
deactivate
echo "Virtual env 'env' Deactivated !"

echo "Reloading App..."
#kill -HUP `ps -C gunicorn fch -o pid | head -n 1`
ps aux |grep gunicorn |grep pg_solar_api | awk '{ print $2 }' |xargs kill -HUP

echo "Deployment Finished !"
