FROM docker.io/jlesage/baseimage-gui:alpine-3.22-v4

COPY ./v2rayN-linux-64/ /app

COPY startapp.sh /startapp.sh

ENV LANG=zh_CN.UTF-8
ENV APP_NAME=v2rayN
ENV ENABLE_CJK_FONT=1
ENV KEEP_APP_RUNNING = 1

RUN chmod +x /app/v2rayN && \
    chmod +x /startapp.sh && \
    # sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk update && \
    apk upgrade && \
    apk add icu libx11 fontconfig libc6-compat libstdc++ libice libsm \
    #font-dejavu