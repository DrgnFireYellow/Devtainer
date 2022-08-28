FROM debian
RUN apt update -y
RUN apt install python3 -y
COPY . /root/devtainer/
WORKDIR /root/devtainer