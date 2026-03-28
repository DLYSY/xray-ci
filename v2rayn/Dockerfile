FROM public.ecr.aws/debian/debian:stable-slim

ENV XDG_RUNTIME_DIR=/tmp/xdg WLR_BACKENDS=headless WLR_LIBINPUT_NO_DEVICES=1 WAYLAND_DISPLAY=wayland-1

ARG XDG_RUNTIME_DIR=/tmp/xdg

# 安装核心组件和测试用的 GUI 应用
RUN apt update && \
    apt dist-upgrade -y --no-install-recommends && \
    apt install --no-install-recommends -y sway wayvnc novnc websockify xwayland fonts-noto-cjk wget unzip jq curl && \
    mkdir /app && \
    cd /app && \
    wget $(curl https://api.github.com/repos/2dust/v2rayN/releases/latest | jq '.assets.[] | select(.name == "v2rayN-linux-64.zip") | .browser_download_url' -r) && \
    unzip /app/v2rayN-linux-64.zip && \
    rm /app/v2rayN-linux-64.zip && \
    chmod +x /app/v2rayN-linux-64/v2rayN && \
    mkdir -p $XDG_RUNTIME_DIR && \
    chmod 0070 $XDG_RUNTIME_DIR && \
    echo '# 设置无头显示器的默认分辨率\n\
output * resolution 1280x720 position 0,0\n\
# 启用 XWayland 以兼容传统的 X11 应用 (如果你的应用原生支持 Wayland 可省略)\n\
xwayland enable\n\
# 启动目标 GUI 应用\n\
exec_always /app/v2rayN-linux-64/v2rayN\n\
exec_always wayvnc 0.0.0.0 5900\n\
exec_always websockify --web /usr/share/novnc 8080 localhost:5900\n\
# 自动将焦点给到新打开的窗口\n\
for_window [class=".*"] focus\n\
for_window [app_id=".*"] focus' | tee /app/sway.conf && \
    echo '{"autoconnect": true, "reconnect": true}' | tee /usr/share/novnc/defaults.json | tee /usr/share/novnc/mandatory.json


EXPOSE 8080
EXPOSE 10808

# 运行启动脚本
ENTRYPOINT ["sway", "-c", "/app/sway.conf"]