from . import fetcher
from . import mtgo_parser
from . import event_parser
from . import file_io

def scrape_event(url):
    html = fetcher.fetch_html(url)
    data = mtgo_parser.extract_mtgo_data(html)
    file_io.save_raw_json(data)

    return {
        "event": event_parser.build_event_row(data),
        "standings": event_parser.parse_standings(data),
        "decklists": event_parser.parse_decklists(data),
        "brackets": event_parser.parse_brackets(data)
    }