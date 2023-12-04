import pika
import output_functions

# Define callback function
def callback(ch, method, properties, body):
    # Decompress data
    decompressed_json = output_functions.decompress_json(body)
    data = output_functions.json_to_awk(decompressed_json)

    # Collect name of data
    name = data[-1]
    
    # Remove name from data
    data = data[:-1]

    # Add data to dictionary
    for category, s in samples.items():
        if name in s['list']:
            data_dict_key = category
            data_dict_value = data
            data_full[data_dict_key] = data_dict_value
    print(f"Received {name}.")
    

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declare the data output queue
channel.queue_declare(queue='data_output')
print('Connected to data_output')

# Import samples & calculate number of expected entries
samples = output_functions.get_samples()
data_expected = output_functions.data_expected(samples)

# Count the number of entries procssed
data_processed = 0

# Define data dictionary
data_full = {}

# Set up a callback function to handle incoming messages
channel.basic_consume(queue='data_output', auto_ack=True, on_message_callback=callback)

# Start listening for messages
print('Waiting for messages. To exit press CTRL+C')

# Loop to consume messages for the number of data_expected
while data_processed <= data_expected:
    print(f"Processed {data_processed} out of {data_expected} entries.")
    channel.start_consuming()
    data_processed += 1
    
# Close connection
connection.close()

# Plot data
output_functions.plot_data(data_full, samples)
