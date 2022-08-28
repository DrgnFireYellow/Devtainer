FROM debian
RUN apt update -y
RUN apt install git python3 -y
COPY . /root/devtainer/
WORKDIR /root/devtainer