FROM python:latest

RUN apt-get update -y && apt-get upgrade -y

RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/
RUN python -m pip install -r requirements.txt
RUN pip install --upgrade openai
RUN pip install torch torchvision torchaudio
CMD bash start
