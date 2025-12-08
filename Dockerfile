FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN mkdir -p /data

ENV DATABASE_PATH=/data/test_users.db

CMD ["python", "app.py"]
