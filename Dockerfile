FROM python:3
RUN pip install colorama
ADD . /
CMD ["python", "./cyk.py"]