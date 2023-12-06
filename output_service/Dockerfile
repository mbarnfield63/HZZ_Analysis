FROM python:latest
ADD output_service/output_service.py output_service/output_functions.py samples.json ./
RUN pip install --upgrade awkward numpy matplotlib pika
CMD ["python", "./output_service.py"]