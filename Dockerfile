FROM ubuntu

#FROM python:2.7
#FROM continuumio/anaconda


ADD . /
env DEBIAN_FRONTEND noninteractive
RUN apt-get update

RUN apt-get install -y gdal-bin python-gdal  python-matplotlib


WORKDIR /



#RUN apt-get install -y build-essential
#WORKDIR /code/gdal
#RUN tar -zxvf gdal-2.0.1.tar.gz
#WORKDIR gdal-2.0.1
#RUN ./configure --with-python
#RUN make
#RUN make install

#RUN conda  install gdal


