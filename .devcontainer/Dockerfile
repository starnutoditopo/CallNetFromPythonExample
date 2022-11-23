FROM python:3.11.0-slim-bullseye
    
# Install .Net	
RUN apt-get update
RUN apt-get -y install wget
#RUN wget https://dot.net/v1/dotnet-install.sh
#RUN chmod 777 ./dotnet-install.sh
#RUN ./dotnet-install.sh -c 6.0

RUN wget https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb

RUN apt-get update && \
    apt-get install -y dotnet-sdk-6.0

RUN pip install pythonnet

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1
