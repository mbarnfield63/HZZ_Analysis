import pika
import json
import awkward as ak

import output_functions

# Define callback function
def callback(ch, method, properties, body):
    # Decompress
    decompressed_json = output_functions.decompress_json(body)
    data = output_functions.json_to_awk(decompressed_json)
    print(data[-1])
    ch.basic_ack(delivery_tag = method.delivery_tag)

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declare the data output queue
channel.queue_declare(queue='data_output')
print('Connected to data_output')

# Set up a callback function to handle incoming messages
channel.basic_consume(queue='data_output', auto_ack=False, on_message_callback=callback)

# Start listening for messages
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()