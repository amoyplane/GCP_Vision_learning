import socket
import requests
import socks


socks5_proxy_host = '127.0.0.1'

socks5_proxy_port = 1080


socks.set_default_proxy(socks.SOCKS5, socks5_proxy_host, socks5_proxy_port)
socket.socket = socks.socksocket


url = 'https://www.google.com'
resp = requests.get(url)


print(resp.status_code)
