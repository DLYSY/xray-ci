from json import dump
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("client_id", help="Client ID for Xray configuration")
args = parser.parse_args()

xray_conf = {
    "inbounds": [
        {
            "port": 80,
            "listen": "0.0.0.0",
            "protocol": "vless",
            "settings": {"clients": [{"id": args.client_id}], "decryption": "none"},
            "streamSettings": {"network": "xhttp", "security": "none"},
            "xhttpSettings": {"path": "/", "mode": "stream-up"},
        }
    ],
    "outbounds": [{"protocol": "freedom"}],
}

with open("config.json", "w") as f:
    dump(xray_conf, f)
