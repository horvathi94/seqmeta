FROM ubuntu:focal

# Install JAVA for webin-cli
RUN apt update --yes 
RUN apt upgrade --yes
RUN apt install curl --yes
RUN apt install default-jre-headless --yes

# Add webin-cli
COPY webin-cli-4.4.0.jar /opt/webin-cli/


# Install Python
RUN apt install software-properties-common --yes
RUN add-apt-repository ppa:deadsnakes/ppa --yes
RUN apt install python3.10 --yes 
RUN apt install python3-pip --yes


# Install Python packages
COPY ./requirements/development.txt /tmp/dev-reqs.txt
RUN pip3 install --no-cache-dir -r /tmp/dev-reqs.txt


# Add seqmeta library to opt
ENV PYTHONPATH "${PYTHONPATH}:/opt/seqmeta"


# Create upload directorires
RUN mkdir -p /home/seqmeta/uploads/samples/assemblies \
	&& mkdir -p /home/seqmeta/uploads/samples/reads


# Expose port for access
EXPOSE 5000



# Switch to work directory
WORKDIR /home/seqmeta/app


CMD ["tail", "-f", "/etc/hosts"]
