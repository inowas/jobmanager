#!/usr/bin/env python
import pika
import sys
import time
import os
from time import sleep
from threading import Thread

PAYLOAD = '{"payload":"payload"}'
RABBITMQ_HOSTNAME = os.getenv("RABBITMQ_HOSTNAME")
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")

def start_worker_thread():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOSTNAME, credentials=pika.credentials.PlainCredentials(username=RABBITMQ_USERNAME, password=RABBITMQ_PASSWORD)))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print('[x] Worker: Waiting for messages')

    def callback(ch, method, properties, body):
        received_payload = body.decode("utf-8")
        print("[x] Worker: Received payload: " + received_payload)
        assert received_payload == PAYLOAD
        ch.basic_ack(delivery_tag = method.delivery_tag)
        exit(0)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback, queue='task_queue')

    channel.start_consuming()



if __name__ == "__main__":
    thread = Thread(target = start_worker_thread)
    thread.start()

    sleep(1)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOSTNAME, credentials=pika.credentials.PlainCredentials(username=RABBITMQ_USERNAME, password=RABBITMQ_PASSWORD)))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_publish(exchange='',
                        routing_key='task_queue',
                        body=PAYLOAD,
                        properties=pika.BasicProperties(
                            delivery_mode = 2, # make message persistent
                        ))
    print("[x] Client: Sent payload: " + PAYLOAD)
    connection.close()