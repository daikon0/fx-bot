FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install pipenv \
    && pipenv install --system

EXPOSE 5000

CMD ["python", "usd_jpy_market.py"]