import json, urllib.parse, re, base64

# 1. Читаем твой ключ из README.md
with open('README.md', 'r', encoding='utf-8') as f:
    my_links = re.findall(r'vless://\S+', f.read())

# 2. Вытаскиваем сервер друга из avto.json и конвертируем в ссылку
friend_links = []
try:
    with open('avto.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for out in data.get("outbounds", []):
        if out.get("protocol") == "vless":
            tag = out.get("tag", "Авто Выбор")
            try:
                vnext = out.get("settings", {}).get("vnext", [{}])[0]
                addr = vnext.get("address", "")
                port = vnext.get("port", 443)
                uuid = vnext.get("users", [{}])[0].get("id", "")
                flow = vnext.get("users", [{}])[0].get("flow", "")
                
                stream = out.get("streamSettings", {})
                params = {
                    "type": stream.get("network", "tcp"),
                    "security": stream.get("security", "none")
                }
                if flow: params["flow"] = flow
                
                if params["security"] == "reality":
                    rs = stream.get("realitySettings", {})
                    params.update({
                        "pbk": rs.get("publicKey", ""),
                        "fp": rs.get("fingerprint", ""),
                        "sni": rs.get("serverName", ""),
                        "sid": rs.get("shortId", ""),
                        "spx": rs.get("spiderX", "/")
                    })
                
                query = urllib.parse.urlencode({k: v for k, v in params.items() if v})
                friend_links.append(f"vless://{uuid}@{addr}:{port}?{query}#{urllib.parse.quote(tag)}")
            except Exception:
                continue
except Exception as e:
    print("Ошибка:", e)

# 3. Объединяем и пакуем в формат Base64 (стандарт для подписок)
all_links = my_links + friend_links
b64_text = base64.b64encode("\n".join(all_links).encode('utf-8')).decode('utf-8')

with open('sub.txt', 'w', encoding='utf-8') as f:
    f.write(b64_text)
