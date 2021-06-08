FROM centos:latest

RUN yum install python3 gcc-c++ python3-devel -y

RUN pip3 install flask keras mysql-connector-python

RUN pip3 install --upgrade pip

RUN pip3 install tensorflow

RUN mkdir /DibetesAPP

WORKDIR /DibetesApp

COPY templates templates/

COPY app.py .

COPY dibetes_model.h5 .

EXPOSE 5000

ENTRYPOINT python3 app.py
