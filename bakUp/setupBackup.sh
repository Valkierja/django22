apt update
apt install cron
crontab -e root
#*  6  *  *  *  /www/sites/ksroido.moe/django22/bakUp/bakUp.sh
