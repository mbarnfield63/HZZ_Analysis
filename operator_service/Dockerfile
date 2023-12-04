FROM python:latest
ADD samples.json infofile.py operator_functions.py operator_run.py /
#ADD wait_for_rabbitmq.sh samples.json infofile.py operator_service/operator_functions.py operator_service/operator_run.py /
RUN pip install --upgrade pika
CMD ["python", "/operator_run.py"]
# RUN chmod +x /wait_for_rabbitmq.sh

# # Set the command to run your application after waiting for RabbitMQ
# CMD ["/bin/bash", "-c", "/wait_for_rabbitmq.sh rabbitmq 5672 python /operator_run.py"]


