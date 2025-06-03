FROM python:3.12-slim-bullseye
ENV TZ=America/Argentina/Buenos_Aires
ENV PYTHONUNBUFFERED=1
ENV FLASK_CONTEXT=production
ENV PATH=$PATH:/home/um/.local/bin

RUN useradd --create-home --home-dir /home/um um
RUN apt-get update 
RUN apt-get install -y python-dev build-essential libpq-dev python3-psycopg2
#Borrar despues de demostrar conexion con otros servicios
RUN apt-get install -y curl htop iputils-ping 
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN rm -rf /var/lib/apt/lists/* /tmp/*
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /home/um
USER um
RUN mkdir app
COPY ./app.py .
COPY ./app ./app
COPY ./uwsgi.ini .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["uwsgi", "--wsgi-file", "app.py", "uwsgi.ini"]
#CMD ["python", "app.py"]