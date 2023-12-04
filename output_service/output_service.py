import output_functions
import pika
import json
import awkward as ak

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declare the data output queue
channel.queue_declare(queue='data_output')
print('Connected to data_output')

# Define callback function
def callback(ch, method, properties, body):

    print(f"Output received: {list(body)}")

# Set up a callback function to handle incoming messages
channel.basic_consume(queue='data_output', auto_ack=True, on_message_callback=callback)

# Start listening for messages
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()