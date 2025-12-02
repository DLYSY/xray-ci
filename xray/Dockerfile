FROM busybox

ADD ./target/x86_64-unknown-linux-musl/release/xray-init /app/xray-init
ADD ./xray /app/xray

RUN chmod +x /app/xray

WORKDIR /app

CMD ["/app/xray-init"]