FROM ubuntu:latest
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /dbconnection-app

COPY requirement.txt .

RUN pip3 install -r requirement.txt

COPY ./db_connection ./db_connection

CMD ["python3", "./db_connection/main.py"]