import worker_functions
import pika
import json
import awkward as ak

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declare the data processing queue
channel.queue_declare(queue='data_processing')

# Declare the data output queue
channel.queue_declare(queue='data_output')

# Set QoS to limit the number of unacknowledged messages to 1
channel.basic_qos(prefetch_count=1)

# Define callback function
def callback(ch, method, properties, body):

    print(f"Worker received: {str(body)}")        
    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

    # process the data
    data = worker_functions.read_file(body)
    print(f'Processed {str(body)}')
    
    # Send the awkward array to the output queue
    ch.basic_publish(exchange='', routing_key='data_output', body=data)

    print(f"Worker sent {str(body)}")

# Set up a callback function to handle incoming messages
# Set auto_ack=False to enable manual acknowledgment
channel.basic_consume(queue='data_processing', on_message_callback=callback)

# Start listening for messages
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()