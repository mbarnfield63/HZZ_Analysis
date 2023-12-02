FROM python:latest
ADD hzz_analysis.py hzz_functions.py infofile.py samples.json ./
RUN pip install --upgrade uproot awkward vector numpy matplotlib
CMD ["python", "./hzz_analysis.py"]
