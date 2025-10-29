from json import dump
from os import environ,_exit

client_id = environ.get("CLIENT_ID")

if client_id is None:
    _exit(1)

xray_conf = {
    "inbounds": [
        {
            "port": 80,
            "listen": "0.0.0.0",
            "protocol": "vless",
            "settings": {"clients": [{"id": client_id}], "decryption": "none"},
            "streamSettings": {"network": "xhttp", "security": "none"},
            "xhttpSettings": {"path": "/", "mode": "stream-up"},
        }
    ],
    "outbounds": [{"protocol": "freedom"}],
}

with open("/etc/xray/config.json", "w") as f:
    dump(xray_conf, f)
