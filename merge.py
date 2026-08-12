import json, re, urllib.parse

# Читаем README.md и ищем ссылку
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'vless://\S+', content)
if not match:
    print("Ссылка vless:// не найдена")
    exit(0)

# Разбираем ссылку на параметры
url = urllib.parse.urlparse(match.group(0))
q = urllib.parse.parse_qs(url.query)
get_q = lambda k: q.get(k, [''])[0]

# Формируем JSON структуру
outbound = {
    "tag": urllib.parse.unquote(url.fragment) if url.fragment else "Мой сервер",
    "protocol": "vless",
    "settings": {
        "vnext": [{
            "address": url.hostname,
            "port": int(url.port) if url.port else 443,
            "users": [{"id": url.username, "encryption": get_q("encryption") or "none"}]
        }]
    },
    "streamSettings": {
        "network": get_q("type") or "tcp",
        "security": get_q("security") or "none"
    }
}

if get_q("flow"): outbound["settings"]["vnext"][0]["users"][0]["flow"] = get_q("flow")

if outbound["streamSettings"]["security"] == "reality":
    outbound["streamSettings"]["realitySettings"] = {
        "publicKey": get_q("pbk"),
        "fingerprint": get_q("fp"),
        "serverName": get_q("sni"),
        "shortId": get_q("sid"),
        "spiderX": get_q("spx") or "/"
    }
elif outbound["streamSettings"]["security"] == "tls":
    outbound["streamSettings"]["tlsSettings"] = {
        "serverName": get_q("sni"),
        "fingerprint": get_q("fp")
    }

if outbound["streamSettings"]["network"] == "ws":
    outbound["streamSettings"]["wsSettings"] = {
        "path": get_q("path") or "/",
        "headers": {"Host": get_q("host") or get_q("sni")}
    }

# Открываем файл друга
with open('avto.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Добавляем твой сервер к серверу друга
if "outbounds" not in data: data["outbounds"] = []
data["outbounds"].append(outbound)

# Сохраняем в новый файл подписки
with open('sub.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
