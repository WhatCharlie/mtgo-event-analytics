import requests
import re
from urllib.parse import urlencode


BASE_URL = "https://www.mtgo.com/decklists"


def build_decklists_url(year=None, month=None, format=None, event_type=None):
    """
    Build an MTGO decklists URL.

    Examples:
        build_decklists_url()
        -> https://www.mtgo.com/decklists

        build_decklists_url(2026, 6, "Pauper", "Challenge")
        -> https://www.mtgo.com/decklists/2026/06?filter=Pauper+Challenge
    """

    if year is None or month is None:
        url = BASE_URL
    else:
        url = f"{BASE_URL}/{year}/{month:02d}"

    filters = []

    if format:
        filters.append(format)

    if event_type:
        filters.append(event_type)

    if filters:
        url += "?" + urlencode({
            "filter": " ".join(filters)
        })

    return url


def get_page_event_urls(page_url):
    """
    Extract event URLs from an MTGO decklists page.
    """

    html = requests.get(page_url).text

    urls = re.findall(
        r'href="(/decklist/[^"]+)"',
        html
    )

    return [
        BASE_URL.replace("/decklists", "") + u
        for u in urls
    ]


def filter_events(urls, event_type):
    """
    Filter event URLs by event type.
    """

    return [
        u for u in urls
        if event_type.lower() in u.lower()
    ]