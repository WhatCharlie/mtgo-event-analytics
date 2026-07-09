import json
from pathlib import Path

def save_raw_json(data, output_dir="../data/raw"):
    """
    Save a raw MTGO event JSON to disk.

    Parameters
    ----------
    data : dict
        Parsed MTGO JSON.

    output_dir : str
        Folder where JSON files should be stored.
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = output_dir / f"{data['event_id']}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)