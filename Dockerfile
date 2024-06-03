FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt /app
COPY detection /app

# RUN apt-get update && \
#     apt-get install -y python3 python3-pip && \
#     pip install -r requirements.txt && \
#     cd detection

RUN apt-get update && apt-get install -y python3 python3-pip

RUN apt-get clean

RUN apt-get install -y openjdk-18-jre

RUN apt-get clean

RUN TMPDIR=/home/user/tmp/ python3 -m pip install -r requirements.txt

# # Download PhoBERT model
# RUN mkdir -p /root/.cache/huggingface/transformers/ && \
#     python3 -c "from transformers import AutoTokenizer, AutoModel; \
#                 AutoTokenizer.from_pretrained('vinai/phobert-large', cache_dir='/root/.cache/huggingface/transformers/'); \
#                 AutoModel.from_pretrained('vinai/phobert-large', cache_dir='/root/.cache/huggingface/transformers/')"

RUN cd detection

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
