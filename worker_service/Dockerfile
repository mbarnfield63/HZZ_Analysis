FROM python:latest
ADD infofile.py processing_data.py worker_functions.py ./

# ADD infofile.py worker_service/processing_data.py worker_service/worker_functions.py ./
RUN pip install --upgrade uproot awkward vector numpy pika
CMD ["python", "./processing_data.py"]