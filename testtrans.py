import socket
import requests
import socks
import json

socks5_proxy_host = '127.0.0.1'

socks5_proxy_port = 1080


socks.set_default_proxy(socks.SOCKS5, socks5_proxy_host, socks5_proxy_port)
socket.socket = socks.socksocket


url = 'https://www.google.com'
#resp = requests.get(url)


# print(resp.status_code)


content = "あのとき。春にここで田中のことを好きになりはじめたのはたしかに。田中が誰のことも好きにならないって言ったからだった。"

language_type = "ja"
url = "https://translation.googleapis.com/language/translate/v2"
data = {
    'key': 'AIzaSyAeQO_0q-juL_-2TCA3nrUkMTCbh9kg3p0',
    'source': language_type,
    'target': 'zh-CN',
    'q': content,
    'format': 'text'
}
headers = {'X-HTTP-Method-Override': 'GET'}
response = requests.post(url, data=data, headers=headers)
# print(response.json())
res = response.json()
# print(res["data"]["translations"][0]["translatedText"])
text = res["data"]["translations"][0]["translatedText"]
print(content)
print(text)
# return text
