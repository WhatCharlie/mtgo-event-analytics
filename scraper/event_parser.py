def build_event_row(data):
    return {
        "event_id": data.get("event_id"),
        "name": data.get("description"),
        "date": data.get("starttime"),
        "format": data.get("format"),
        "players": int(data["player_count"]["players"])
        if data.get("player_count")
        else None
    }


def parse_standings(data):
    rows = []

    for s in data.get("standings", []):
        rows.append({
            "event_id": data.get("event_id"),
            "player": s.get("login_name"),
            "rank": int(s["rank"]) if s.get("rank") else None,
            "score": int(s["score"]) if s.get("score") else None,
            "omwp": float(s["opponentmatchwinpercentage"])
                if s.get("opponentmatchwinpercentage")
                else None,
            "gwp": float(s["gamewinpercentage"])
                if s.get("gamewinpercentage")
                else None,
            "ogwp": float(s["opponentgamewinpercentage"])
                if s.get("opponentgamewinpercentage")
                else None,
            "eliminated": s.get("eliminated") == "true"
        })

    return rows


def parse_decklists(data):
    rows = []

    for d in data.get("decklists", []):
        rows.append({
            "event_id": data.get("event_id"),
            "player": d.get("player"),
            "loginid": d.get("loginid"),
            "main_deck": d.get("main_deck", []),
            "sideboard": d.get("sideboard_deck", [])
        })

    return rows


def parse_brackets(data):
    rows = []

    for round_block in data.get("brackets", []):
        round_idx = round_block.get("index")

        for match in round_block.get("matches", []):
            players = match.get("players", [])

            if len(players) < 2:
                continue

            p1, p2 = players

            rows.append({
                "event_id": data.get("event_id"),
                "round": round_idx,
                "player1": p1.get("player"),
                "player2": p2.get("player"),
                "winner": (
                    p1.get("player")
                    if p1.get("winner")
                    else p2.get("player")
                )
            })

    return rows