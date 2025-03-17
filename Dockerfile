FROM python:3.10-slim
RUN apt-get update

WORKDIR /home

COPY extensions.conf sip.conf /etc/asterisk/
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "scriptflask.py"]
