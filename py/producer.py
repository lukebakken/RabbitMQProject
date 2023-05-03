#!/usr/bin/env python
import pika
import sys
import PIL
import requests
from io import BytesIO
import matplotlib.pyplot as plt


req = requests.get ("https://raw.githubusercontent.com/carletto27/RabbitMQProject/2-next-steps/test.jpg")
image = Image.open(BytesIO(req.content))


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="topic", exchange_type="topic")

routing_key = sys.argv[1] if len(sys.argv) > 2 else "anonymous.info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange="topic", routing_key=routing_key, body=image)
print(" [Image] Sent %r" % (routing_key))
connection.close()
