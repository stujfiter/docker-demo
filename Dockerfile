FROM ubuntu

RUN apt-get update
RUN apt-get install python -y
RUN apt-get install python-pip -y
RUN easy_install web.py

COPY helloweb.py .

CMD ["python","helloweb.py","8080"]
