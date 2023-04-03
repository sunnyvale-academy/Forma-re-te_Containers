FROM ubuntu:latest
RUN  apt-get update
RUN  apt-get --assume-yes install wget
RUN  wget https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_linux-x64_bin.tar.gz
RUN  tar -zxvf openjdk-17.0.2_linux-x64_bin.tar.gz
COPY sorgente_java /home/sorgente_java
WORKDIR /home/sorgente_java
RUN /jdk-17.0.2/bin/javac Dockertest.java
CMD  /jdk-17.0.2/bin/java ${JAVA_OPT} Dockertest ${APP_OPT}
