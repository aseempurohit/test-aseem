FROM ubuntu:latest
MAINTAINER Anuyog Chauhan "anuyog.chauhan@aricent.com
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
##RUN dd if=/dev/zero of=file.txt count=1024 bs=2572864 
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["service-time.py"]
