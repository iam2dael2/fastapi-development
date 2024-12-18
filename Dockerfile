FROM python:3.12.8
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ARG RAILWAY_SERVICE_NAME="fastapi-development"
CMD ["hypercorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]