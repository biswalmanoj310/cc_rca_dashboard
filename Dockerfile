# -----------------------------
# Dockerfile for Flask RCA App
# -----------------------------
FROM python:3.12-slim

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
