FROM ubuntu:latest
MAINTAINER Anuyog Chauhan "anuyog.chauhan@aricent.com
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN cat requirements.txt | while read PACKAGE; do pip install --proxy=http://proxy.example.com "$PACKAGE"; done
ENTRYPOINT ["python"]
CMD ["service-time.py"]
