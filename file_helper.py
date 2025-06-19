class FileLoadError(Exception):
    pass

def load_data(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        raise FileLoadError(f"File not found: {file_path}")
    except IOError as e:
        raise FileLoadError(f"Error reading file {file_path}: {e}")

def clean_data(data: list[str]) -> list[str]:
    return [line.strip() for line in data if line.strip()]