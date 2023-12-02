FROM python:latest
ADD concat_plot.py plotting.py samples.json ./
RUN pip install --upgrade awkward numpy matplotlib
CMD ["python", "./concat_plot.py"]