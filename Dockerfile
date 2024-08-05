FROM python:3.10.14-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["sh", "-c"]
CMD ["python3 -m src.main.api"]
