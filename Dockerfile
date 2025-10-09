FROM ghcr.io/xtls/xray-core:latest

ADD ./config.json /etc/xray/config.json

ENTRYPOINT [ "/usr/local/bin/xray","-confdir", "/etc/xray/"]