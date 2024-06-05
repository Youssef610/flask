from flask import jsonify
import requests
import json
import re

url = "http://pass-gpt.nowtechai.com/api/v1/pass"


def ai(msg):
    payload = json.dumps({
        "contents": [
            {
                "role": "system",
                "content": "You are SCI bot, a large language model trained by sci team."
            },
            {
                "role": "user",
                "content": msg
            }
        ]
    })

    headers = {
        'User-Agent': "Ktor client",
        'Connection': "Keep-Alive",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'Key': "ya/kfyhrEWBBIq6jysr2PnTXCD1gMyvXQI4B4DrykMYKenfZeKmPw0x+kgSC/XbpUctoYk0GtwLnr8nfWs25Bw==",
        'TimeStamps': "1717601117827",
        'Accept-Charset': "UTF-8"
    }
    response = requests.post(url, data=payload, headers=headers)
    json_strings = re.findall(r'data:({.*?})', response.text)
    res = "".join(json.loads(
        js)["content"] for js in json_strings if json.loads(js)["status"] == "stream")
    return jsonify({"aiResponse": res})
