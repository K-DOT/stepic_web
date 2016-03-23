#!/bin/sh
echo "Recreating database"
sudo service mysql restart
mysql -uroot -e "drop database ask;" || true
mysql -uroot -e "create database ask;"
echo "Copying NGINX config file"
sudo cp web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo service nginx restart
echo "[Re]starting gunicorn"
killall -9 gunicorn || true
cd web/ask && gunicorn ask.wsgi -b "0.0.0.0:8000" --max-requests 1 > /dev/null 2>&1 &
web/ask/manage.py syncdb
