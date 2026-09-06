from pathlib import Path

def sort_file(file_path: Path):
    pass

def move_file(file_path: Path):
    pass

def load_source_folder(source_path: Path) -> list[Path]:
    source_files = []
    for file in source_path.iterdir():
        if file.is_file:
            source_files.append(file)
    print(f"{len(source_files)} files found in '{source_path}'")
    return source_files
