FROM ubuntu

RUN apt update && apt install -y python3 \
    && apt clean

WORKDIR /opt

COPY app.py .

CMD ["python3", "app.py"]
