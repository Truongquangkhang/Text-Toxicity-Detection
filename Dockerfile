FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt /app
COPY detection /app

# RUN apt-get update && \
#     apt-get install -y python3 python3-pip && \
#     pip install -r requirements.txt && \
#     cd detection

RUN apt-get update && apt-get install -y python3 python3-pip

RUN apt-get install openjdk-18-jre

RUN pip install -r requirements.txt

RUN cd detection

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
