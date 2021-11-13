FROM python:3.8.8

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x /app/scripts/run_server.sh
ENV FLASK_ENV=docker
ENTRYPOINT /app/scripts/run_server.sh