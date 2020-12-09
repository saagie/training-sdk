FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY app.py /app

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
