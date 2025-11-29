import sys
import shutil
from pathlib import Path


def copy_and_sort_files(src: str, dst: str = "dist"):
    try:
        source_dir = Path(src)
        destination_dir = Path(dst)
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, destination_dir)

            elif item.is_file():
                extension = item.suffix[1:]  # Get extension without dot
                if not extension:
                    extension = "no_extension"
                target_dir = destination_dir / extension
                target_dir.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.copy2(item, target_dir / item.name)
                    print(f"Copied: {item} -> {target_dir / item.name}")
                except OSError as e:
                    print(f"Error copying {item}: {e}")

    except OSError as e:
        print(f"Error accessing {source_dir}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)
    if len(sys.argv) > 2:
        copy_and_sort_files(sys.argv[1], sys.argv[2])
    else:
        copy_and_sort_files(sys.argv[1])
