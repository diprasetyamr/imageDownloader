FROM python
RUN adduser --disabled-password --gecos '' docker
USER docker
ENTRYPOINT ["/bin/bash", "/home/docker/run.sh"]
