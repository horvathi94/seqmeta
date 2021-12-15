FROM python:3.6 AS development
MAINTAINER horvathi

WORKDIR /temp
COPY ./requirements/development.txt dev-requirements.txt
RUN pip3 install --no-cache-dir -r dev-requirements.txt

RUN mkdir -p /uploads/samples/assemblies \ 
	& mkdir -p /uploads/samples/reads


EXPOSE 5000

WORKDIR /app
CMD ["tail", "-f", "/app/uwsgi.ini"]

# Uncomment this line to run the app on container startup in development mode.
#CMD ["python3", "./wsgi.py"]


FROM development AS production

COPY ./requirements/production.txt prod-requirements.txt
RUN pip3 install --no-cache-dir -r prod-requirements.txt



WORKDIR /app
COPY ./app /app

RUN groupadd --gid 5000 pyman \
	&& useradd --uid 5000 --gid 5000 --shell /bin/bash pyman \
	&& chown -R pyman:pyman /temp

USER pyman
EXPOSE 5000


CMD ["uwsgi", "uwsgi.ini"]
