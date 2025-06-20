FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/static && cd src && python manage.py collectstatic --noinput

CMD ["gunicorn", "--chdir", "src", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
