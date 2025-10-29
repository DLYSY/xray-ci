FROM teddysun/xray:latest

RUN apk add python3

ADD ./generate_config.py /app/generate_config.py

WORKDIR /app

ENTRYPOINT ["/usr/bin/python", "/app/generate_config.py", "&&", "/usr/bin/xray", "-confdir", "/etc/xray"]