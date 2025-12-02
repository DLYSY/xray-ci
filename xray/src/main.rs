use serde_json::json;
use std::{
    env, fs,
    os::unix::{fs::PermissionsExt, process::CommandExt},
    process::Command,
};

fn main() -> Result<(), String> {
    let client_id = env::var("CLIENT_ID").map_err(|_| "找不到 CLIENT_ID 环境变量".to_string())?;
    let config_json = json!({
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

    fs::write("/config.json", config_json.to_string())
        .map_err(|_| "无法写入config.json".to_string())?;

    let error = Command::new("/xray")
        .args(["run", "-c", "/config.json"])
        .exec();

    Err(format!("无法启动主程序:{}", error))
}
