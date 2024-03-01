FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD . /app

COPY ./requrements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


COPY . /app 

EXPOSE 8000

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# CMD ["python", "manage.py","collectstatic","migrate"]
CMD ["python", "manage.py","runserver"]


# RUN chmod +x /code/local-entrypoint.sh







