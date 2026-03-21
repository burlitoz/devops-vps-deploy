
FROM python:3.12
RUN apt-get update && apt-get install -y curl && useradd -m appuser
WORKDIR /app
COPY /app/requirements.txt .
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY --chown=appuser:appuser app/ .
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]