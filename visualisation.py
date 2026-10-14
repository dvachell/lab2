from pathlib import Path
import matplotlib.pyplot as plt
from demo_w2 import schema, records
from model import Schema, CoercingValidator

CHART_PATH = Path(__file__).parent / "bledy_wg_pola.png"

def count_errors_per_field() -> dict:
    counts = {}
    for field in schema.schema_fields:
        one_field_validator = CoercingValidator(Schema([field]))
        errors = 0
        for record in records:
            if not one_field_validator.validate(record).is_valid:
                errors += 1
        counts[field.name] = errors
    return counts


if __name__ == "__main__":
    errors_per_field = count_errors_per_field()

    fig, ax = plt.subplots()
    ax.bar(list(errors_per_field.keys()), list(errors_per_field.values()))
    ax.set_title("Bledy walidacji wg pola schematu (rekordy z W2)")
    ax.set_xlabel("Pole schematu")
    ax.set_ylabel("Liczba bledow")

    fig.savefig(CHART_PATH)
    plt.show()
