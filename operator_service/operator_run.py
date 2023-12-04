import pika
import operator_functions

samples = operator_functions.get_samples() # retrieve samples dict
list_urls = operator_functions.list_samples(samples) # retrieve list of samples

# Establish connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declare the data processing queue
channel.queue_declare(queue='data_processing')

for url in list_urls:
    channel.basic_publish(exchange='',
                            routing_key='data_processing',
                            body=url)
    print(f"Operator sent {url}.")

print("Sent all URLs.")
# Close connection to the RabbitMQ server
connection.close()