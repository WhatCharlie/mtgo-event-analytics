import json

def extract_mtgo_data(html):
    start = html.find("window.MTGO.decklists.data")
    start = html.find("{", start)

    depth = 0
    for i in range(start, len(html)):
        if html[i] == "{":
            depth += 1
        elif html[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break

    return json.loads(html[start:end])