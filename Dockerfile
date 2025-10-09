FROM teddysun/xray:latest

ADD ./config.json /etc/xray/config.json

ENTRYPOINT [ "/usr/bin/xray","-confdir", "/etc/xray"]