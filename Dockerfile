FROM apache/airflow:2.7.2

USER root
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

COPY requirements.txt /requirements.txt
RUN chmod 777 /requirements.txt

USER airflow
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt