FROM python:3.6 AS development
MAINTAINER horvathi94 

WORKDIR /temp
COPY ./development/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /uploads/samples/assemblies \ 
	& mkdir -p /uploads/samples/reads


EXPOSE 5000

WORKDIR /app
#CMD ["python3", "./wsgi.py"]
CMD ["tail", "-f", "/etc/passwd"]


FROM development AS production

COPY ./production/requirements.txt prod-requirements.txt
RUN pip3 install --no-cache-dir -r prod-requirements.txt


WORKDIR /app
COPY ./app /app

RUN groupadd --gid 5000 pyman \
	&& useradd --uid 5000 --gid 5000 --shell /bin/bash pyman \
	&& chown -R pyman:pyman /temp

USER pyman

CMD ["python3", "/app/wsgi.py"]
