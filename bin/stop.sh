#!/bin/sh

pid1=`ps -ef|grep "uwsgi"| grep -v "grep"|awk '{print $2}'`

if [ "$pid1" != "" ]
then
	    kill -9 ${pid1}
	        echo "stop uwsgi--${pid1} complete"
    else
	    echo "uwsgi is not run"

		fi

