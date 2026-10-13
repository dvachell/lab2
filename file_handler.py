from pathlib import Path
import json


def load_records(path_to_file: Path):
    path = Path(path_to_file)
    if path.suffix == ".json":
        with open(path_to_file, encoding="utf-8") as file:
            records = json.load(file)
            if not isinstance(records, list):
                raise ValueError(f'File {path.name} should contain a list of records, got {type(records).__name__}')
            return records
        
    elif path.suffix == ".csv":
        raise ValueError("csv is not supported")

    elif path.suffix == ".pkl":
        raise ValueError("pkl is not supported")
    
    else :
        raise ValueError("file extension is not supported")


def save_report(report: dict, path_to_file: Path):
    with open(path_to_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)

