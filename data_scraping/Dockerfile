FROM python:3.9-alpine

WORKDIR /scraper

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "scraper.py" ]