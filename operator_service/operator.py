import pika
import operator_functions

if __name__ == '__main__':
    samples = operator_functions.get_samples() # retrieve samples dict
    list_urls = operator_functions.list_samples(samples) # retrieve list of samples

    # Establish connection to the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the data processing queue
    channel.queue_declare(queue='data_processing')

    for url in list_urls:
        channel.basic_publish(exchange='',
                              routing_key='data_processing',
                              body=url)
    
    # Close connection to the RabbitMQ server
    connection.close()


