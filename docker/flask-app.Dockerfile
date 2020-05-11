FROM python:3.6-stretch

COPY ./requirements/api.txt /opt/project/requirements.txt
COPY ./app /opt/project/app
COPY ./settings/api.py /opt/project/settings/api.py
COPY ./wsgi.py /opt/project/wsgi.py

WORKDIR /opt/project/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn -w 4 --bind 0.0.0.0:8000 wsgi:app