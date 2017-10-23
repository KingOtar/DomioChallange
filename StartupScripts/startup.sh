#!/usr/bin/env bash
cd /opt/interview/kitten_counter/
/root/.virtualenvs/cats/bin/celery worker -A  app.celery --loglevel=info -f /tmp/celeryError -E&
service apache2 start
tail -f /dev/null
