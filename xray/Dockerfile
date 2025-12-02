FROM busybox

ADD ./target/x86_64-unknown-linux-musl/release/xray-init /app/xray-init
ADD ./xray /app/xray

WORKDIR /app

CMD ["/app/xray-init"]