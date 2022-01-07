FROM python:3.7

WORKDIR /home/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 6060

RUN useradd -M auth0
USER auth0

CMD ["gunicorn"]
