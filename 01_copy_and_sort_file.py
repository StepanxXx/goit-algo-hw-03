import sys
import shutil
from pathlib import Path


def get_unique_filename(target_dir: Path, filename: str) -> str:
    """Генерує унікальне ім'я файлу, якщо файл з таким іменем вже існує."""
    target_path = target_dir / filename
    if not target_path.exists():
        return filename
    
    # Розділяємо ім'я файлу та розширення
    stem = target_path.stem
    suffix = target_path.suffix
    
    # Додаємо числовий суфікс до імені файлу
    counter = 1
    while True:
        new_filename = f"{stem}_{counter}{suffix}"
        new_path = target_dir / new_filename
        if not new_path.exists():
            return new_filename
        counter += 1


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
                    # Отримуємо унікальне ім'я файлу
                    unique_filename = get_unique_filename(target_dir, item.name)
                    target_path = target_dir / unique_filename

                    shutil.copy2(item, target_path)
                    if unique_filename != item.name:
                        print(f"Copied: {item} -> {target_path} (renamed to avoid conflict)")
                    else:
                        print(f"Copied: {item} -> {target_path}")
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
