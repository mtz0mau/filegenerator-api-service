FROM python:3.12.0-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /app

COPY .env.example .env

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# start app with gunicorn and uvicorn worker
CMD ["gunicorn", "-c", "gunicorn_conf.py", "app.main:app"]
