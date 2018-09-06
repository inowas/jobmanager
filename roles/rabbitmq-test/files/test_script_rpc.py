#!/usr/bin/env python
import pika
import uuid
from threading import Thread
from time import sleep

RABBITMQ_HOST = 'rabbitmq'
PAYLOAD = '{"payload":"payload"}'

def start_server_thread():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=pika.credentials.PlainCredentials(username="admin", password="admin")))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')

    def on_request(ch, method, props, body):
        print("[x] Server: Received Request with payload: " + body.decode("utf-8"))
        assert body.decode("utf-8") == PAYLOAD
        response = body
        ch.basic_publish(exchange='',
                        routing_key=props.reply_to,
                        properties=pika.BasicProperties(correlation_id=props.correlation_id),
                        body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        channel.stop_consuming()
    

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='rpc_queue')
    print("[x] Server: Awaiting RPC request")
    channel.start_consuming()

class RpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=pika.credentials.PlainCredentials(username="admin", password="admin")))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to = self.callback_queue, correlation_id = self.corr_id,),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

if __name__ == "__main__":
    thread = Thread(target = start_server_thread)
    thread.start()

    sleep(1)

    rpc = RpcClient()
    print("[x] Client: Send request to server with payload: " + PAYLOAD)
    response = rpc.call(PAYLOAD)
    print("[x] Client: Got response with payload: " + response.decode("utf-8") )
    assert response.decode("utf-8") == PAYLOAD
    exit(0)
