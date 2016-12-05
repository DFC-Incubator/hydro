FROM ubuntu

ADD . /

env DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install -y gdal-bin python-gdal  python-matplotlib 
COPY matplotlibrc /etc/matplotlibrc

#CMD ["ls","-r","/"]
#WORKDIR ./code

#CMD ./PopulationVsSoilMoisture.scr

