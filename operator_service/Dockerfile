FROM python:latest
ADD samples.json infofile.py operator_service/operator_functions.py operator_service/operator.py /
RUN pip install --upgrade pika
CMD ["python", "/operator.py"]