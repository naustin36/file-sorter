from pathlib import Path
from config import *

config = load_config()
destination = Path(config["destination_folder"]).expanduser()
file_categories = config["media_types"]

def sort_file(file: Path) -> None:
    for category in file_categories:
        if file.suffix in file_categories[category]:
            final_destination = destination.joinpath(category)
            move_file(file, final_destination)

def move_file(file: Path, destination_path: Path) -> None:
    print(f"Moving {file.name} to '{destination_path}'")
    if not destination_path.exists():
        destination_path.mkdir()
    final_destination = destination_path.joinpath(file.name)
    file.rename(final_destination)

def load_source_folder(source_path: Path) -> list[Path]:
    source_files = []
    for file in source_path.iterdir():
        if file.is_file:
            source_files.append(file)
    print(f"{len(source_files)} files found in '{source_path}'")
    return source_files
