#!/bin/sh

( sleep 10 ; \

rabbitmqctl add_user admin {{ admin_user_password }}
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

) &
rabbitmq-server $@
