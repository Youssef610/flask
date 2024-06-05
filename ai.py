from flask import jsonify
import requests
import json
import re

url = "http://pass-gpt.nowtechai.com/api/v1/pass"


def ai(msg):



  url = "https://chatgpt-au.vulcanlabs.co/api/v1/token"

  payload = json.dumps({
    "device_id": "57C8AC7D51346473",
    "order_id": "",
    "product_id": "",
    "purchase_token": "",
    "subscription_id": ""
  })

  headers = {
    'User-Agent': "Chat Smith Android, Version 3.6.2(548)",
    'Accept': "application/json",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/json",
    'x-vulcan-application-id': "com.smartwidgetlabs.chatgpt",
    'x-vulcan-request-id': "9149487891713168904149"
  }
  while True:
    try:
      response = requests.post(url, data=payload, headers=headers,timeout=5)
      break
    except:
      continue


  auth=response.json()["AccessToken"]

  url = "https://prod-smith.vulcanlabs.co/api/v6/chat"
  payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "user": "57C8AC7D51346473",
    "messages": [
      {
        "role": "system",
        "content": "You are Sci Chat, a personal AI. Your words are never longer than 2000 words."    },
      {
        "role": "user",
        "content":f"{msg}"
      }
    ],
    "nsfw_check": True
  })

  headers = {
    'User-Agent': "Chat Smith Android, Version 3.6.2(548)",
    'Accept': "application/json",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/json",
    'x-firebase-appcheck': "AppCheck",
    'authorization': f"Bearer {auth}",
    'x-vulcan-application-id': "com.smartwidgetlabs.chatgpt",
    'x-vulcan-request-id': "9149487891713142621674"
  }

  response = requests.post(url, data=payload, headers=headers)
  return jsonify({"aiResponse": response.json()["choices"][0]["Message"]["content"]})
