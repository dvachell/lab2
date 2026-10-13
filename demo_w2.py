from model import SchemaField, Schema, CoercingValidator

schema = Schema([
    SchemaField("name", str, True),
    SchemaField("age", int, True),
    SchemaField("email", str, False),
])

records = [
    # poprawne
    {"name": "Jan", "age": 25, "email": "jan@email.com"},
    {"name": "Anna", "age": 31},                                    # brak pola opcjonalnego
    {"name": "Piotr", "age": 40, "email": "p@email.com", "x": 1},  # dodatkowe pole
    # poprawne po koercji
    {"name": "Kasia", "age": "28", "email": "k@email.com"},        # "28" -> 28
    {"name": "Tomek", "age": 33.9},                                 # 33.9 -> 33
    # bledne
    {"age": 22, "email": "brak@email.com"},                         # brak wymaganego name
    {"name": "Ola"},                                                # brak wymaganego age
    {"name": "Marek", "age": "abc"},                                # nie da sie skonwertowac
    {"name": "Ewa", "age": None},                                   # None
    {"name": "Adam", "age": [30]},                                  # lista zamiast liczby
]

if __name__ == "__main__":
    validator = CoercingValidator(schema)
    for i, record in enumerate(records, start=1):
        result = validator.validate(record)
        status = "OK  " if result.is_valid else "Error"
        print(f"{i:>2}. {status} {record}")
        for error in result.errors:
            print(f"    > {error}")
