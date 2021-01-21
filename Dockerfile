FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install pipenv psycopg2

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /app

COPY pyproject.toml /app/
COPY poetry.lock /app/
RUN /root/.poetry/bin/poetry config virtualenvs.create false
RUN /root/.poetry/bin/poetry install

RUN mkdir --parents /app/instance
RUN mkdir --parents /app-mnt

COPY docker/prestart.sh /app/
COPY docker/uwsgi.ini /app/
COPY docker/mail_alias_manager.conf /app/instance/config.py
COPY mail_alias_manager /app/mail_alias_manager
COPY migrations /app/migrations

ENV FLASK_APP mail_alias_manager
ENV MODE production
ENV MAIL_ALIAS_MANAGER_SETTINGS /app-mnt/mail_alias_manager.conf

VOLUME ["/app-mnt"]
