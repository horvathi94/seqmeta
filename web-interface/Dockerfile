FROM python:3.10 AS development

# Create seqmeta user and group
RUN groupadd seqmeta \
	&& useradd --shell /bin/bash --create-home --gid seqmeta seqmeta
USER seqmeta 

# Install required python packages
COPY ./requirements/development.txt /tmp/dev-reqs.txt
RUN pip3 install --no-cache-dir -r /tmp/dev-reqs.txt --user 


# Create upload directories
RUN mkdir -p /home/seqmeta/uploads/samples/assemblies \
	&& mkdir -p /home/seqmeta/uploads/samples/reads


# Expose port for access
EXPOSE 5000

ENV PYTHONPATH "${PYTHONPATH}:/opt/seqmeta"


# Switch to work directory
WORKDIR /home/seqmeta/app


# Run a command on container spinup
CMD ["tail","-f", "/etc/hosts"]
