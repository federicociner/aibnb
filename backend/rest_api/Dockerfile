FROM python:3.6
RUN mkdir -p /opt/airbnb/
workdir /opt/airbnb
COPY ./requirements.txt /opt/airbnb/requirements.txt
COPY . /opt/airbnb/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
