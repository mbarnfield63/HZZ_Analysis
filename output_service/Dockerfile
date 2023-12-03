FROM python:latest
ADD output_service.py output_functions.py samples.json ./
RUN pip install --upgrade awkward numpy matplotlib
CMD ["python", "./concat_plot.py"]