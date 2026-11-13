FROM python:3.11-slim
WORKDIR /app
COPY calculator.py .
COPY test_calculator.py .
CMD ["python", "test_calculator.py"]
