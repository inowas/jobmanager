#!/bin/sh

( sleep 10 ; \

rabbitmqctl add_user admin {{ admin_user_password }}
rabbitmqctl add_user worker {{ worker_user_password }}
rabbitmqctl add_user backend {{ backend_user_password }}
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
rabbitmqctl set_permissions -p / worker ".*" ".*" ".*"
rabbitmqctl set_permissions -p / backend ".*" ".*" ".*"

) &
rabbitmq-server $@
