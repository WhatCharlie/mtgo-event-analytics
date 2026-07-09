import json
from pathlib import Path
import os
import pandas as pd

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

def update_csv(new_data, filepath, unique_column):
    """
    Append new data to an existing CSV and remove duplicates.
    """

    if os.path.exists(filepath):
        old_data = pd.read_csv(filepath)
        combined = pd.concat([old_data, new_data], ignore_index=True)
    else:
        combined = new_data

    combined = combined.drop_duplicates(
        subset=unique_column,
        keep="last"
    )

    combined.to_csv(filepath, index=False)

    return combined