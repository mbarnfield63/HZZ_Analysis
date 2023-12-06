import pika
import zlib
import json
import awkward as ak
import output_functions

# Define callback function
def callback(ch, method, properties, body):
    
    global data_processed
    global data_expected

    # Decompress data
    decompressed_json = zlib.decompress(body)

    # Decode data
    data_with_identifier = json.loads(decompressed_json)

    # Extract awkward array and name
    name = data_with_identifier.get('data_name', None)
    data = data_with_identifier.get('data', None)

    data = ak.from_iter(data)

    # Add data to dictionary
    for category, s in samples.items():
        if name in s['list']:
            data_dict_key = category
            data_full[data_dict_key].append(data)  # Append data to the list

    print(f"Received {name}.")

    data_processed += 1
    print(f"Processed {data_processed} out of {data_expected} datasets.")
    if data_processed == data_expected:
        channel.stop_consuming()
    

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

# Define data dictionary, original keys from samples, empty lists as values
data_full = {category: [] for category in samples}

# Set up a callback function to handle incoming messages
channel.basic_consume(queue='data_output', auto_ack=True, on_message_callback=callback)

# Start listening for messages
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# Loop through data_full dictionary keys and concatenate lists to awkward arrays
for category, data_list in data_full.items():
    data_full[category] = ak.concatenate(data_list)

# Plot data
output_functions.plot_data(data_full, samples)

# Close connection
connection.close()