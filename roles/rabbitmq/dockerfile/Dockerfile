FROM rabbitmq:3.7-management

ADD ["plugins/accept-*", \
     "plugins/prometheus-*", \
     "plugins/prometheus_httpd-*",\
     "plugins/prometheus_cowboy-*", \
     "plugins/prometheus_process_collector-*", \
     "plugins/prometheus_rabbitmq_exporter-*", \
     "/usr/lib/rabbitmq/plugins/"]
RUN chmod a+r /usr/lib/rabbitmq/plugins/prometheus*.ez /usr/lib/rabbitmq/plugins/accept*.ez \
    && rabbitmq-plugins enable --offline prometheus accept prometheus_rabbitmq_exporter prometheus_process_collector prometheus_httpd prometheus_cowboy
