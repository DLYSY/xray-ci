FROM teddysun/xray:latest

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk add python3

ADD ./generate_config.py /app/generate_config.py
ADD ./run.sh /app/run.sh

WORKDIR /app

CMD ["/bin/sh", "/app/run.sh"]