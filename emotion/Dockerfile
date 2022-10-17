# Pull Python image from Docker Hub
FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /emotions-app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./vision ./vision

CMD ["python3", "./vsion/main.py"]