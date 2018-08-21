FROM python
RUN adduser --disabled-password --gecos '' docker
USER docker
WORKDIR /home/docker
#CMD cd /home/docker
