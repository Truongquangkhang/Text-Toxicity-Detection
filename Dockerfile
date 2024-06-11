FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
COPY detection /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN cd detection

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
