#!/bin/sh

PRG="$0"
while [ -h "$PRG" ]; do
  ls=`ls -ld "$PRG"`
  link=`expr "$ls" : '.*-> \(.*\)$'`
  if expr "$link" : '/.*' > /dev/null; then
    PRG="$link"
  else
    PRG=`dirname "$PRG"`/"$link"
  fi
done
APP_DIR=`dirname "$PRG"`
cd "$APP_DIR/../"
APP_DIR=`pwd`
echo "starting now..."

pid=`ps -ef|grep "uwsgi"| grep -v "grep"|awk '{print $2}'`

if [ "$pid" != "" ]
then
                echo "uwsgi already run, stop it first ————${pid}"
                        kill -9 ${pid}
                fi

nohup pipenv run uwsgi --ini $APP_DIR/oms/uwsgi.ini >/dev/null 2>&1 &
systemctl restart nginx


echo "start succeed!"
