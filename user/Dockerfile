FROM python:3.9-slim

WORKDIR /app

COPY ./user/.env ./user/.env

COPY ./user/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./user/ ./user/

CMD ["python", "-m", "user.main"]