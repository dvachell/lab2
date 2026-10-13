from pathlib import Path
import json

def load_records(path_to_file: str):
    path = Path(path_to_file)
    if path.suffix == ".json":
        with open(path_to_file, encoding="utf-8") as file:
            records = json.load(file)
            if not isinstance(records, list):
                raise ValueError(f'File {path.name} is not json')
            return records
        
    elif path.suffix == ".csv":
        raise ValueError("csv is not supported")
    
    elif path.suffix == ".pkl":
        raise ValueError("pkl is not supported")
    
    else :
        raise ValueError("file extension is not supported")

