import requests
import zipfile

req = requests.get("https://api.github.com/repos/2dust/v2rayN/releases/latest")

linux_asset_url = next(filter(lambda x: x["name"] == "v2rayN-linux-64.zip",req.json()["assets"]))["browser_download_url"]

with open("v2rayn.zip","wb") as f:
    f.write(requests.get(linux_asset_url).content)

with zipfile.ZipFile("v2rayn.zip","r") as f:
    f.extractall(".")

# system("chmod +x startapp.sh")
# system("chmod +x ./v2rayN-linux-64/v2rayN")