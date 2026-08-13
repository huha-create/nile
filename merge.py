import json, re, urllib.parse

# 1. Читаем твой VLESS-ключ
with open('README.md', 'r', encoding='utf-8') as f:
    match = re.search(r'vless://\S+', f.read())
if not match: exit(0)

url = urllib.parse.urlparse(match.group(0))
q = urllib.parse.parse_qs(url.query)
get_q = lambda k: q.get(k, [''])[0]

my_outbound = {
    "tag": "proxy",
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
if get_q("flow"): my_outbound["settings"]["vnext"][0]["users"][0]["flow"] = get_q("flow")
if my_outbound["streamSettings"]["security"] == "reality":
    my_outbound["streamSettings"]["realitySettings"] = {
        "publicKey": get_q("pbk"), "fingerprint": get_q("fp"), "serverName": get_q("sni"),
        "shortId": get_q("sid"), "spiderX": get_q("spx") or "/"
    }
elif my_outbound["streamSettings"]["security"] == "tls":
    my_outbound["streamSettings"]["tlsSettings"] = {"serverName": get_q("sni"), "fingerprint": get_q("fp")}
if my_outbound["streamSettings"]["network"] == "ws":
    my_outbound["streamSettings"]["wsSettings"] = {"path": get_q("path") or "/", "headers": {"Host": get_q("host") or get_q("sni")}}

# 2. Создаем твой личный независимый профиль
my_profile = {
    "remarks": "🇷🇺 Белые списки №1",
    "outbounds": [
        my_outbound,
        {"protocol": "freedom", "tag": "direct"},
        {"protocol": "blackhole", "tag": "block"}
    ]
}

# 3. Открываем профиль друга (Автовыбор)
with open('avto.json', 'r', encoding='utf-8') as f:
    friend_profile = json.load(f)
    friend_profile["remarks"] = "⚡ Авто Выбор"

# 4. Лазейка Xray: объединяем профили в JSON Array (Массив)
# Германские (Автовыбор) ставим первыми, российский — последним
final_array = [friend_profile, my_profile]

# 5. Сохраняем итоговый массив
with open('sub.json', 'w', encoding='utf-8') as f:
    json.dump(final_array, f, indent=2, ensure_ascii=False)
