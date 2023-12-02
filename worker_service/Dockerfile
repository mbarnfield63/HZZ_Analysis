FROM python:latest
ADD infofile.py processing_data.py worker_functions.py ./
RUN pip install --upgrade uproot awkward vector numpy
CMD ["python", "./processing_data.py"]