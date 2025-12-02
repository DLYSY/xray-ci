use serde_json::json;
use std::{env, fs, os::unix::{fs::PermissionsExt, process::CommandExt}, process::Command};

fn main() -> Result<(), String> {
    let client_id = env::var("CLIENT_ID").map_err(|_| "找不到 CLIENT_ID 环境变量".to_string())?;
    let j = json!({
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
    });

    fs::write("/app/config.json", j.to_string()).map_err(|_|{"无法写入config.json".to_string()})?;

    // let mut perms = fs::metadata("/app/xray").unwrap().permissions();
    // perms.set_mode(mode);

    let error = Command::new("/app/xray")
        .args(["run", "-c", "/app/config.json"])
        .exec();

    Err(format!("无法启动主程序:{}", error))
}
