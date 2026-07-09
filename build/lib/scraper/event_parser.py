def build_event_row(data):
    return {
        "event_id": data["event_id"],
        "name": data["description"],
        "date": data["starttime"],
        "format": data["format"],
        "players": int(data["player_count"]["players"])
    }

def parse_standings(data):
    rows = []
    for s in data["standings"]:
        rows.append({
            "event_id": data["event_id"],
            "player": s["login_name"],
            "rank": int(s["rank"]),
            "score": int(s["score"]),
            "omwp": float(s["opponentmatchwinpercentage"]),
            "gwp": float(s["gamewinpercentage"]),
            "ogwp": float(s["opponentgamewinpercentage"]),
            "eliminated": s["eliminated"] == "true"
        })
    return rows

def parse_decklists(data):
    rows = []

    for d in data["decklists"]:
        rows.append({
            "event_id": data["event_id"],
            "player": d["player"],
            "loginid": d["loginid"],
            "main_deck": d["main_deck"],
            "sideboard": d.get("sideboard_deck", [])
        })

    return rows

def parse_brackets(data):
    rows = []

    for round_block in data["brackets"]:
        round_idx = round_block["index"]

        for match in round_block["matches"]:
            p1, p2 = match["players"]

            rows.append({
                "event_id": data["event_id"],
                "round": round_idx,
                "player1": p1["player"],
                "player2": p2["player"],
                "winner": p1["player"] if p1["winner"] else p2["player"]
            })

    return rows

