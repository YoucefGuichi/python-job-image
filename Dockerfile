from python:latest

RUN pip install pika

copy main.py main.py

cmd ["python3", "main.py"]