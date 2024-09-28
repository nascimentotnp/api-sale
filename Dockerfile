FROM python:3.10-slim

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app/app:$PYTHONPATH
COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "-b", "0.0.0.0:8080", "app.run:app"]