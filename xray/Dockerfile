FROM scratch

ADD ./target/x86_64-unknown-linux-musl/release/xray-init /xray-init
ADD ./xray /xray

CMD ["/xray-init"]