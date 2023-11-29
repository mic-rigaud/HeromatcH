FROM debian

ARG HEROMATCH_BOT_TOKEN
ARG HEROMATCH_ADMINS


RUN apt-get update -yq  \
    && apt-get install -y python3-pip python3 net-tools graphviz traceroute locales \
    && sed -i -e "s/# fr_FR.UTF-8.*/fr_FR.UTF-8 UTF-8/" /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=fr_FR.UTF-8 \
    && apt-get clean -y

RUN apt-get install -y python3-poetry

ADD . /app/

WORKDIR /app

VOLUME /app/log
VOLUME /app/data

RUN cp ./install/config-docker.py ./config.py && poetry install


CMD poetry run invoke install && poetry run invoke start-local