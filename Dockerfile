FROM python:3.11-slim

WORKDIR /

ENV GOOGLE_APPLICATION_CREDENTIALS='./secrets/credentials'

COPY requirements.txt requirements.txt
COPY wsgi_server.py wsgi_server.py 
COPY server.sh server.sh

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

RUN chmod +x server.sh
ENTRYPOINT ["./server.sh"]