FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY entrypoint.py .

ENTRYPOINT [ "python" ]

CMD [ "entrypoint.py" ]
