ARG UPSTREAM_VERSION=latest
FROM cktechno/django-base:dc89b09

WORKDIR /usr/src/app
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

RUN chmod +x /usr/src/app/run/*.sh

CMD ["uwsgi", "--processes=5" ,"--http", "0.0.0.0:8000", "--buffer-size", "8192" , "--protocol", "uwsgi", "--module", "server.wsgi:application"]
ENTRYPOINT ["/usr/src/app/run/entrypoint.sh"]
