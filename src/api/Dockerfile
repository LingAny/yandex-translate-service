FROM python:latest

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /api
WORKDIR /api
RUN python setup.py install
RUN rm -rf /api

COPY ./main.py /usr/local/ling_any/main.py
WORKDIR /usr/local/ling_any

ENV DB_HOST postgres
ENV DB_NAME translator
ENV DB_USER translator
ENV DB_PASS translator
ENV DB_PORT 5432
ENV WEB_PORT 80

CMD /usr/local/bin/gunicorn --worker-connections 512 --worker-class aiohttp.GunicornWebWorker -b :$WEB_PORT --reload main:app