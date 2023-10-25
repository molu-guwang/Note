#!/bin/bash
server_name=$1
server_pid=`ps -ef  | grep java | grep $server_name | awk '{ print $2}'`
if [ ! $server_pid ]; then
	echo "null"
else
	kill -15 $server_pid
  sleep 20
  cd ./backend/$server_name
  nohup java -jar rrcc-$server_name.jar
fi

sleep 30
if [ ! $server_pid ]; then
	echo "Start service failed"
else
	echo "Start service succeed"
fi
