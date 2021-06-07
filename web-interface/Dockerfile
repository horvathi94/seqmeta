FROM python:3.6 AS development
MAINTAINER horvathi94 

WORKDIR /temp
COPY ./development/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

WORKDIR /app
#CMD ["python3", "./wsgi.py"]
#CMD["uwsg"]
CMD ["tail", "-f", "/etc/passwd"]


FROM development AS production

COPY ./production/requirements.txt prod-requirements.txt
RUN pip3 install --no-cache-dir -r prod-requirements.txt

#COPY ./code ./
WORKDIR /app/code
#COPY ./production/wsgi.ini ./wsgi.ini

RUN groupadd --gid 5000 pyman \
	&& useradd --uid 5000 --gid 5000 --shell /bin/bash pyman \
	&& mkdir /app/temp \
	&& chown -R pyman:pyman /app/temp

USER pyman

CMD ["uwsgi", "wsgi.ini"]
