FROM python:3.6
MAINTAINER horvathi94 


WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


EXPOSE 5000

#COPY ./code /app

RUN groupadd --gid 5000 pyman \
	&& useradd --uid 5000 --gid 5000 --shell /bin/bash pyman \
	&& mkdir /app/temp \
	&& chown -R pyman:pyman /app/temp

USER pyman

CMD ["python3", "./code/main.py"]
#CMD ["tail", "-f", "/etc/hosts"]
