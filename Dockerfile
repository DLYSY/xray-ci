FROM ghcr.io/xtls/xray-core:latest

ADD ./config.json /usr/local/etc/xray/config.json

ENTRYPOINT [ "/usr/local/bin/xray","-confdir", "/usr/local/etc/xray/"]