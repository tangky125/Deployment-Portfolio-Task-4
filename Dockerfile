FROM python:3.12-slim
WORKDIR /app
COPY analyzer.py .
CMD ["python", "analyzer.py"]