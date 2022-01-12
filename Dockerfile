FROM python:3.7.12-slim-buster@sha256:00d0a225c8cd0a1102f98f6e044d59cc44064c5681c1bbc34abbdba5a41c1ac4 as build

RUN mkdir /app
RUN mkdir /install

RUN useradd -m developer

RUN groupadd auth0

RUN usermod -a -G auth0 developer

RUN chown -R developer:auth0 /app
RUN chown -R developer:auth0 /install

WORKDIR /app

USER developer

COPY requirements.txt .

RUN pip install --no-warn-script-location -U pip
RUN sh -c 'pip install --no-warn-script-location --prefix=/install -r requirements.txt'

COPY authz authz/
COPY common common/
COPY hello_world hello_world/
COPY messages_api messages_api/
COPY gunicorn.conf.py manage.py ./


FROM python:3.7.12-slim-buster@sha256:00d0a225c8cd0a1102f98f6e044d59cc44064c5681c1bbc34abbdba5a41c1ac4

COPY --from=build /install /usr/local
COPY --from=build /app /app

RUN useradd -m developer

RUN groupadd auth0

RUN usermod -a -G auth0 developer

RUN chown -R developer:auth0 /app

WORKDIR /app

USER developer

EXPOSE 6060

CMD ["gunicorn"]
