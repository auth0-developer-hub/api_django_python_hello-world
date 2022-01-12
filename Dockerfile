FROM python:3.8.12-slim-buster@sha256:55ef3d2132dec7f372f4d63fbec0027e23388ab072533edbba9ca213a053c9cb as build
RUN mkdir /app
RUN mkdir /packages
RUN useradd -m developer
RUN groupadd auth0
RUN usermod -a -G auth0 developer
RUN chown -R developer:auth0 /app
RUN chown -R developer:auth0 /packages
WORKDIR /app
USER developer
COPY requirements.txt .
RUN pip install --disable-pip-version-check -r requirements.txt --target /packages
COPY authz authz/
COPY common common/
COPY hello_world hello_world/
COPY messages_api messages_api/
COPY gunicorn.conf.py manage.py ./


FROM gcr.io/distroless/python3@sha256:eb773dd9d39f0becdab47e2ef5f1b10e2988c93a40ac8d32ca593096b409d351
COPY --from=build /packages /packages
COPY --from=build /app /app
WORKDIR /app
USER 1000
ENV PYTHONPATH=/packages
CMD ["/packages/gunicorn/app/wsgiapp.py","hello_world.wsgi:application"]
