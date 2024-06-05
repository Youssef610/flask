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
    # Regular expression to find all content values
    pattern = r'"content":"(.*?)"'

    # Find all content values
    contents = re.findall(pattern, response.text)

    # Combine and clean the content values
    combined_content = "".join(contents)
    final_sentence = " ".join(combined_content.strip().split())

    return jsonify({"aiResponse": final_sentence})
