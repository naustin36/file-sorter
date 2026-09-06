from pathlib import Path
import json

CONFIG = Path("config.json")
DEFAULT_CONFIG = {
    "source_folder":None,
    "destination_folder":None,
    "photo": [".jpg", ".jpeg", ".png", ".webp"],
    "video": [".mp4", ".webm"],
    "gif": [".gif"]
}

def load_config() -> dict:
    if not CONFIG.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG, "w") as f:
        json.dump(config, f, indent=4)

def validate_config(config) -> dict:
    if not config["source_folder"]:
        raise Exception("No source folder set in config.json")
    if not config["destination_folder"]:
        config["destination_folder"] = config["source_folder"]
    return config
