#!/usr/bin/env bash

SELF_PATH=`cd $(dirname $0); pwd -P;`
read -e -p "Enter IP address of your config server？/ 请输入您服务器的 IP 地址:" \
    -i "39.105.214.245" SERVER_IP
read -e -p "Enter the deploy port of your config? / 请输出您需要部署的服务器 IP 地址："\
    -i "80" SERVER_PORT
read -e -p "Enter domain name of your config server / 请输入指向您服务器的域名:" \
    -i "www.nkchatbot.com" DOMAIN_NAME
read -e -p "What is the name of your project / 您希望您项目的名称叫什么(please do not leave blank):" \
    -i "ServerAPI" PROJECT_NAME

cat << _EOF_ > tmp
server {
    listen ${SERVER_PORT};
    server_name ${SERVER_IP} ${DOMAIN_NAME};
    charset     utf-8;
    client_max_body_size 75M;

    root ${SELF_PATH};
    index index.html index.htm index.nginx-debian.html;

    error_page 404 /404.html;
    error_page 500 /500.html;

    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
}
_EOF_

sudo mv tmp /etc/nginx/sites-available/${PROJECT_NAME}.conf
sudo ln -sf /etc/nginx/sites-available/${PROJECT_NAME}.conf /etc/nginx/sites-enabled/
sudo chown -R www-data:www-data .
sudo systemctl restart nginx
