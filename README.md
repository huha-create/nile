#subscription-userinfo: upload=1; download=1; total=1; expire=999999999999999
#profile-title: Sulim vpn 🏎️
#profile-update-interval: 1
#subscription-update-interval: 1
#announce: Если VPN не работает нажмите 🔄 , после ⏱️ и выберите сервер с наименьшим показателем ms!
#support-url: https://wa.me/79639864491
#profile-web-page-url: https://wa.me/79639864491
happ://routing/bypass-lan-and-cn?name=Bypass+LAN+and+CN

{
  "burstObservatory" : {
    "pingConfig" : {
      "connectivity" : "",
      "destination" : "http:\/\/www.gstatic.com\/generate_204",
      "interval" : "1m",
      "sampling" : 1,
      "timeout" : "3s"
    },
    "subjectSelector" : [
      "proxy"
    ]
  },
  "dns" : {
    "queryStrategy" : "UseIP",
    "servers" : [
      "1.1.1.1",
      "1.0.0.1"
    ]
  },
  "inbounds" : [
    {
      "listen" : "127.0.0.1",
      "port" : 10808,
      "protocol" : "socks",
      "settings" : {
        "auth" : "noauth",
        "udp" : true
      },
      "sniffing" : {
        "destOverride" : [
          "http",
          "tls",
          "quic"
        ],
        "enabled" : true,
        "routeOnly" : false
      },
      "tag" : "socks"
    },
    {
      "listen" : "127.0.0.1",
      "port" : 10809,
      "protocol" : "http",
      "settings" : {
        "allowTransparent" : false
      },
      "sniffing" : {
        "destOverride" : [
          "http",
          "tls",
          "quic"
        ],
        "enabled" : true,
        "routeOnly" : false
      },
      "tag" : "http"
    }
  ],
  "log" : {
    "access" : "\/private\/var\/mobile\/Containers\/Shared\/AppGroup\/E3336D99-7384-47F7-83F5-CE4E39385500\/Library\/Application Support\/Xray\/logs\/access.log",
    "dnsLog" : true,
    "loglevel" : "Warning"
  },
  "outbounds" : [
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "176.108.245.184",
            "port" : 25565,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "chrome",
          "publicKey" : "4i3aVyDqVM-6wbiUQnfaXfBwQkNXxQp5YQZ4SRVbL2I",
          "serverName" : "gp.x5.ru"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "78.159.245.124",
            "port" : 1111,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "chrome",
          "publicKey" : "YuhNgtj_Tf8WNLiSB2bNJKPvfwmqa6PNRpbP8TvNkzA",
          "serverName" : "api-maps.yandex.ru"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-2"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "176.108.243.162",
            "port" : 1505,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "chrome",
          "publicKey" : "2YCYnPqsLgEgKPyjwE0MJJ0xV13Daeg3WN7wDrAdD3I",
          "serverName" : "gp.x5.ru"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-3"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "176.108.243.211",
            "port" : 1255,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "chrome",
          "publicKey" : "kTDSBp4QGP4ob2GsBXkJAsSggJ6thuIuyfJQajX_RW4",
          "serverName" : "www.vk.com"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-4"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "78.159.245.118",
            "port" : 25567,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "qq",
          "publicKey" : "tsxzBG6xHNl1Nu8XPpd3hWk_zPGrpFrv2Z-difc3nGY",
          "serverName" : "iv.kommersant.ru",
          "shortId" : "a5bd715847213387"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-5"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "78.159.245.53",
            "port" : 25567,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "qq",
          "publicKey" : "tsxzBG6xHNl1Nu8XPpd3hWk_zPGrpFrv2Z-difc3nGY",
          "serverName" : "iv.kommersant.ru",
          "shortId" : "a5bd715847213387"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-6"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "46.8.209.201",
            "port" : 25565,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "qq",
          "publicKey" : "Pw1EUU1hud5uvtfySGyGy5vV38bYIiQzDx-cDQoAdk0",
          "serverName" : "img.perekrestok.ru",
          "shortId" : "a5bd715847213387"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-7"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "84.201.152.58",
            "port" : 25565,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "qq",
          "publicKey" : "Pw1EUU1hud5uvtfySGyGy5vV38bYIiQzDx-cDQoAdk0",
          "serverName" : "img.perekrestok.ru",
          "shortId" : "a5bd715847213387"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-8"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "78.159.245.70",
            "port" : 1111,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "chrome",
          "publicKey" : "YuhNgtj_Tf8WNLiSB2bNJKPvfwmqa6PNRpbP8TvNkzA",
          "serverName" : "api-maps.yandex.ru"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-9"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "78.159.245.45",
            "port" : 25565,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "qq",
          "publicKey" : "Pw1EUU1hud5uvtfySGyGy5vV38bYIiQzDx-cDQoAdk0",
          "serverName" : "img.perekrestok.ru",
          "shortId" : "a5bd715847213387"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-10"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "78.159.245.43",
            "port" : 25567,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "qq",
          "publicKey" : "tsxzBG6xHNl1Nu8XPpd3hWk_zPGrpFrv2Z-difc3nGY",
          "serverName" : "iv.kommersant.ru",
          "shortId" : "a5bd715847213387"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-11"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "176.123.165.17",
            "port" : 27015,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "chrome",
          "publicKey" : "3ui1m1pntYNW-iQfGRkM-nF-tZM4SzKbQM_R1jWT6yg",
          "serverName" : "cdp.x5.ru"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-12"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "78.159.245.42",
            "port" : 27015,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "qq",
          "publicKey" : "gXormNFH1ALjMoyAybpx9oLvTok6lmMdR5b4Flnif3s",
          "serverName" : "adaptation.sfera.x5.ru"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-13"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "81.94.148.18",
            "port" : 25567,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "95ca49d5-7fca-4943-b71f-ede65e04d562"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "qq",
          "publicKey" : "tsxzBG6xHNl1Nu8XPpd3hWk_zPGrpFrv2Z-difc3nGY",
          "serverName" : "iv.kommersant.ru",
          "shortId" : "a5bd715847213387"
        },
        "security" : "reality",
        "tcpSettings" : {

        }
      },
      "tag" : "proxy-14"
    },
    {
      "protocol" : "freedom",
      "tag" : "direct"
    },
    {
      "protocol" : "blackhole",
      "tag" : "block"
    }
  ],
  "remarks" : "🇷🇺  Авто-выбор | Анти-глушилки LTE",
  "routing" : {
    "balancers" : [
      {
        "fallbackTag" : "direct",
        "selector" : [
          "proxy"
        ],
        "strategy" : {
          "settings" : {
            "baselines" : [
              "1s"
            ],
            "expected" : 2,
            "maxRTT" : "1s",
            "tolerance" : 0.01
          },
          "type" : "leastLoad"
        },
        "tag" : "Super_Balancer"
      }
    ],
    "domainMatcher" : "hybrid",
    "domainStrategy" : "IPIfNonMatch",
    "rules" : [
      {
        "outboundTag" : "direct",
        "protocol" : [
          "bittorrent"
        ],
        "type" : "field"
      },
      {
        "balancerTag" : "Super_Balancer",
        "network" : "tcp,udp",
        "type" : "field"
      }
    ]
  }
}

{
  "dns" : {
    "queryStrategy" : "UseIP",
    "servers" : [
      "1.1.1.1",
      "1.0.0.1"
    ]
  },
  "inbounds" : [
    {
      "listen" : "127.0.0.1",
      "port" : 10808,
      "protocol" : "socks",
      "settings" : {
        "auth" : "noauth",
        "udp" : true
      },
      "sniffing" : {
        "destOverride" : [
          "http",
          "tls",
          "quic"
        ],
        "enabled" : true,
        "routeOnly" : false
      },
      "tag" : "socks"
    },
    {
      "listen" : "127.0.0.1",
      "port" : 10809,
      "protocol" : "http",
      "settings" : {
        "allowTransparent" : false
      },
      "sniffing" : {
        "destOverride" : [
          "http",
          "tls",
          "quic"
        ],
        "enabled" : true,
        "routeOnly" : false
      },
      "tag" : "http"
    }
  ],
  "log" : {
    "access" : "\/private\/var\/mobile\/Containers\/Shared\/AppGroup\/E3336D99-7384-47F7-83F5-CE4E39385500\/Library\/Application Support\/Xray\/logs\/access.log",
    "dnsLog" : true,
    "loglevel" : "Warning"
  },
  "outbounds" : [
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "95.85.253.57",
            "port" : 8090,
            "users" : [
              {
                "encryption" : "none",
                "flow" : "",
                "id" : "8d3318ea-8d24-4d5f-99d6-fd779d738e3c"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "ws",
        "security" : "none",
        "wsSettings" : {
          "headers" : {
            "Host" : "rukr.speedload.ru"
          },
          "path" : "\/ws"
        }
      },
      "tag" : "proxy"
    },
    {
      "protocol" : "freedom",
      "tag" : "direct"
    },
    {
      "protocol" : "blackhole",
      "tag" : "block"
    }
  ],
  "remarks" : "🇪🇺 Авто выбор сервера",
  "routing" : {
    "domainMatcher" : "hybrid",
    "domainStrategy" : "IPIfNonMatch",
    "rules" : [
      {
        "outboundTag" : "direct",
        "protocol" : [
          "bittorrent"
        ],
        "type" : "field"
      }
    ]
  }
}
