FROM python:alpine3.18

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "__init__.py"]