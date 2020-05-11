FROM python:3.6-stretch

COPY ./requirements/crawler.txt /opt/project/requirements.txt
COPY ./settings/crawler.py /opt/project/settings/crawler.py
COPY ./news /opt/project/news
COPY ./scrapy.cfg /opt/project/scrapy.cfg

WORKDIR /opt/project/

RUN pip install -r requirements.txt

CMD [ "scrapy", "crawl", "news" ]