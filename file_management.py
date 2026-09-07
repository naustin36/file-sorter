from pathlib import Path
from config import *

config = load_config()
destination = Path(config["destination_folder"]).expanduser()

def sort_file(file: Path):
    if file.suffix in config["photo"]:
        print(f"Image Found: {file.name}")
        final_destination = destination.joinpath("photo")
        print(f"Destination folder: {final_destination}")
        move_file(file, final_destination)
    if file.suffix in config["video"]:
        print(f"Video Found: {file.name}")
        final_destination = destination.joinpath("video")
        print(f"Destination folder: {final_destination}")
        move_file(file, final_destination)
    if file.suffix in config["gif"]:
        print(f".gif found: {file.name}")
        final_destination = destination.joinpath("gif")
        print(f"Destination folder: {final_destination}")
        move_file(file, final_destination)

def move_file(file: Path, destination_path: Path):
    print("Moving file:",file.name)
    print("Moving to:",destination_path)
    if not destination_path.exists():
        destination_path.mkdir()
    final_destination = destination_path.joinpath(file.name)
    print("TEST/",final_destination)
    file.rename(final_destination)

def load_source_folder(source_path: Path) -> list[Path]:
    source_files = []
    for file in source_path.iterdir():
        if file.is_file:
            source_files.append(file)
    print(f"{len(source_files)} files found in '{source_path}'")
    return source_files
