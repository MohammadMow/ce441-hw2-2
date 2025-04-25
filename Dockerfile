FROM python:3.12-slim

RUN pip install fastapi uvicorn

WORKDIR /app

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
