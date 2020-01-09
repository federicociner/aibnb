FROM python:3.6
RUN mkdir -p /opt/airbnb/
RUN apt-get update
RUN  apt-get install mysql-client -y
WORKDIR /opt/airbnb
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["/bin/bash"]
