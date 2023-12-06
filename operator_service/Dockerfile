FROM python:latest
ADD samples.json infofile.py operator_service/operator_functions.py operator_service/operator_run.py /
RUN pip install --upgrade pika
CMD ["python", "/operator_run.py"]



