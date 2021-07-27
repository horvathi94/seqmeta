FROM python:3.6 AS development
MAINTAINER horvathi94 

WORKDIR /temp
COPY ./requirements/development.txt dev-requirements.txt
RUN pip3 install --no-cache-dir -r dev-requirements.txt

RUN mkdir -p /uploads/samples/assemblies \ 
	& mkdir -p /uploads/samples/reads


EXPOSE 5000

WORKDIR /app
#CMD ["python3", "./wsgi.py"]
CMD ["tail", "-f", "/etc/passwd"]


FROM development AS production

COPY ./requirements/production.txt prod-requirements.txt
RUN pip3 install --no-cache-dir -r prod-requirements.txt


RUN pip3 install gunicorn[gevent]


WORKDIR /app
COPY ./app /app

RUN groupadd --gid 5000 pyman \
	&& useradd --uid 5000 --gid 5000 --shell /bin/bash pyman \
	&& chown -R pyman:pyman /temp

USER pyman
EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info

#CMD ["python3", "/app/wsgi.py"]
