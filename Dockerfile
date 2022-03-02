FROM ubuntu AS base
WORKDIR "/app"
RUN apt update && apt install -y python3 python3-pip

FROM base AS app
COPY *.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD ["python3","server.py"]
