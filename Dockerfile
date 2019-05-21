FROM phusion/baseimage:0.11
MAINTAINER dave.defijter@iota.org
EXPOSE 5000

RUN add-apt-repository universe
RUN apt update
RUN apt -y install python3 python3-venv python3-pip supervisor

RUN mkdir -p /captcha/src
COPY . /captcha/src/
WORKDIR /captcha/src
RUN python3 -m venv /captcha/env
RUN /captcha/env/bin/pip install -r /captcha/src/requirements.txt
RUN cp /captcha/src/conf/supervisor.conf /etc/supervisor/conf.d/captcha.conf

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD service supervisor start && supervisorctl tail -f captcha
