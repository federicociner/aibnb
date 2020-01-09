FROM python:3.6
RUN mkdir -p /opt/airbnb/
WORKDIR /opt/airbnb
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["/bin/bash"]
