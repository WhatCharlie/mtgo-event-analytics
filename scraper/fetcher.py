import requests
import time

def fetch_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    time.sleep(1)
    return r.text