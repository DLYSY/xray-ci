from json import dump
from os import environ

xray_conf = {
    "inbounds": [
        {
            "port": 80,
            "listen": "0.0.0.0",
            "protocol": "vless",
            "settings": {"clients": [{"id": environ.get("CLIENT_ID")}], "decryption": "none"},
            "streamSettings": {"network": "xhttp", "security": "none"},
            "xhttpSettings": {"path": "/", "mode": "stream-up"},
        }
    ],
    "outbounds": [{"protocol": "freedom"}],
}

with open("config.json", "w") as f:
    dump(xray_conf, f)
