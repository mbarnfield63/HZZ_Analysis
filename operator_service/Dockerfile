FROM python:latest
ADD ../samples.json ../infofile.py operator_functions.py operator.py ./
RUN pip install --upgrade pika
CMD ["python", "./operator.py"]