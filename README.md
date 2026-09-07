### File Sorter CLI Tool

When run, moves all selected filetypes from the source folder to the destination folder.

The source and destination folders, the specific folders files are sorted into, and which filetypes are sorted can all be configured in config.json.

The config file is created automatically on first run, but no default source or destination folder is set. You must add a source folder before the tool can be used:

  "source_folder": "(path to your source folder)",
  "destination_folder": null,

If you do not set the destination folder, it will use the source folder as the destination for the file type sub-folders.

To change the name of the folder a file type is saved to, add file types to sort, or add a new media type, edit config.json as shown:

"media_types": {
        "(new folder name here)": [
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
            "(new .ext)"
        ],
        "video": [
            ".mp4",
            ".webm"
        ],
        "gif": [
            ".gif"
        ],
        "(new media type)": [
            "(new .ext)",
            "(new .ext)"
        ]
    },
