FROM python:3.10

WORKDIR /home/

RUN git clone https://github.com/woohaen88/web_programming.git

WORKDIR /home/web_programming/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-sg!9x9@w28+hj!a@r6^(f49el(kzeu$9b#w2!hrez2ymlqx=hh" > .env

RUN python manage.py makemigrations &&\
    python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
