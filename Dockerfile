FROM python:3.10

WORKDIR /home/

RUN git clone https://github.com/woohaen88/web_programming.git

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/web_programming/

RUN pip install -r requirements.txt

RUN python manage.py collectstatic