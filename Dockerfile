FROM python:3.9-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "task_management.py"]
