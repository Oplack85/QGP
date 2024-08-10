FROM python:3.10-alpine as builder

RUN pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python", "main.py"]
