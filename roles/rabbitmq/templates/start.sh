#!/bin/sh

( sleep 10 ; \

rabbitmqctl add_user admin {{ admin_user_password }}
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

rabbitmqctl add_user worker {{ worker_user_password }}
rabbitmqctl set_permissions -p / worker ".*" ".*" ".*"

rabbitmqctl add_user backend {{ backend_user_password }}
rabbitmqctl set_permissions -p / backend ".*" ".*" ".*"

# TODO: Remove this, its there for migrations reasons
rabbitmqctl add_user inowas_user inowas_password
rabbitmqctl add_vhost inowas_host
rabbitmqctl set_permissions -p inowas_host inowas_user ".*" ".*" ".*"
rabbitmqctl set_user_tags inowas_user administrator

) &
rabbitmq-server $@
