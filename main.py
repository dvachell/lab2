import json
from pathlib import Path

import demo_data
import file_handler
from model import Schema, SchemaField, CoercingValidator

REPORTS_DIR = Path(__file__).parent / "reports"

schema = Schema([
    SchemaField("name", str, True),
    SchemaField("age", int, True),
    SchemaField("email", str, False),
])


def process_file(file: Path, validator: CoercingValidator):
    try:
        records = file_handler.load_records(file)
    except FileNotFoundError:
        print(f"Brak pliku: {file.name}")
        return
    except json.JSONDecodeError as e:
        print(f"Plik {file.name} nie jest poprawnym JSON-em: {e}")
        return
    except ValueError as e:
        print(f"Niepoprawna struktura pliku {file.name}: {e}")
        return

    print(f"Wczytano {len(records)} rekordow z pliku {file.name}")

    valid_records_ctr = 0
    invalid_records_ctr = 0
    errors = []
    for index, record in enumerate(records):
        res = validator.validate(record)
        if res.is_valid:
            valid_records_ctr += 1
        else:
            invalid_records_ctr += 1
            errors.append({"indeks": index, "bledy": res.errors})

    print(f"Zwalidowano: {valid_records_ctr} poprawnych, {invalid_records_ctr} z bledami")

    report = {
        "plik_wejsciowy": file.name,
        "liczba_rekordow": len(records),
        "poprawne": valid_records_ctr,
        "z_bledami": invalid_records_ctr,
        "bledy": errors,
    }
    report_path = REPORTS_DIR / f"raport_{file.stem}.json"
    file_handler.save_report(report, report_path)
    print(f"Zapisano raport: {report_path.name}")


if __name__ == "__main__":
    demo_data.make_files()
    demo_data.make_broken_files()
    REPORTS_DIR.mkdir(exist_ok=True)

    validator = CoercingValidator(schema)

    files = sorted(demo_data.DATA_DIR.iterdir())
    files.append(demo_data.DATA_DIR / "nie_ma.json")
    for file in files:
        process_file(file, validator)
        print()
