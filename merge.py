import json, re, urllib.parse

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'vless://\S+', content)
if not match: exit(0)

url = urllib.parse.urlparse(match.group(0))
q = urllib.parse.parse_qs(url.query)
get_q = lambda k: q.get(k, [''])[0]

my_tag = "🇷🇺 Белые списки №1"

my_outbound = {
    "tag": my_tag,
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

with open('avto.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if "outbounds" not in data: data["outbounds"] = []
data["outbounds"].append(my_outbound)

# Глубокая интеграция твоего сервера в механизм автовыбора
if "burstObservatory" in data and "subjectSelector" in data["burstObservatory"]:
    if my_tag not in data["burstObservatory"]["subjectSelector"]:
        data["burstObservatory"]["subjectSelector"].append(my_tag)
elif "observatory" in data and "subjectSelector" in data["observatory"]:
    if my_tag not in data["observatory"]["subjectSelector"]:
        data["observatory"]["subjectSelector"].append(my_tag)

with open('sub.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
