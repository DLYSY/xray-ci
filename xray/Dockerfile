FROM scratch

ADD ./target/x86_64-unknown-linux-musl/release/xray-init /xray-init
ADD ./Xray-linux-64/xray /xray

WORKDIR /

CMD ["/xray-init"]