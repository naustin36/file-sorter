from pathlib import Path
from file_management import *
from config import *

def main():
    print("Media File Sorter")

    try:
        config = load_config()
    except Exception as e:
        print(e)
        return

    source_folder = Path(config["source_folder"]).expanduser()
    source_files = load_source_folder(source_folder)
    destination = Path(config["destination_folder"]).expanduser()

    # Temporary until feature for selecting file types is completed
    file_categories = config["media"]

    for file in source_files:
        try:
            # Only move files, not directories
            if file.is_file():
                sort_file(file, destination, file_categories)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

def filter_file_list(source_files: list[Path]):
    pass
