import requests
import re

def get_all_urls():
    url = "https://www.mtgo.com/decklists"
    html = requests.get(url).text

    urls = re.findall(r'href="(/decklist/[^"]+)"', html)

    return ["https://www.mtgo.com" + u for u in urls]

def filter_events(urls, event_type):
    return [u for u in urls if event_type in u]