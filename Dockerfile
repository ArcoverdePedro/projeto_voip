FROM python:3.10
RUN apt-get update &&\
  apt install asterisk -y &&\
  rm -rf /var/lib/apt/lists/*
WORKDIR /home

COPY extensions.conf sip.conf /etc/asterisk/
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD scriptflask.py
