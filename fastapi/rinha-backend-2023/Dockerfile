FROM bitnami/python:3.11.1
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9999
CMD python -m uvicorn main:app --host 0.0.0.0 --port 9999 --reload