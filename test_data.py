import json 
import random
from collections import Counter

names = ["Jan", "Anna", "Piotr", "Kasia", "Tomek"]
    
def generate_valid_data(names: list[str], number_of_records: int) -> list[dict]:
    generated_records = []
    for record_number in range(number_of_records):
        name = random.choice(names)
        age = random.randint(17,80)
        email = f'{name}{random.randint(0,99)}@email.com'
        record = {
            "name": name,
            "age": age,
            "email": email
            }
        generated_records.append(record)
    return generated_records
        

def corrupt_records(records: list[dict], corr_data_perc: float) -> Counter:
    stats = Counter()
    for record in records:
        if random.random() <= corr_data_perc:
            mutation = random.choice(["convertible_type","non_convertible_type", "remove_req", "remove_opt", "no_data", "extra_field"])
            if mutation == "convertible_type":
                record["age"] = str(record["age"])
            elif mutation == "non_convertible_type":
                record["age"] = "abc"
            elif mutation == "remove_req":
                del record[random.choice(["name", "age"])]
            elif mutation == "remove_opt":
                del record["email"]
            elif mutation == "no_data":
                record["age"] = None
            elif mutation == "extra_field":
                record["extra"] = "unexpected"
            stats[mutation] += 1
    return stats


def make_broken_files():
    broken_files = {
        "broken_truncated.json": '[{"name": "Jan", "age": 25}, {"name": "Anna", "ag',
        "broken_empty.json": '',
        "broken_not_json.json": 'to nie jest json',
        "broken_not_list.json": '{"name": "Jan", "age": 25}',
        "broken_not_dicts.json": '[1, 2, "x"]',
        "broken_mixed.json": '[{"name": "Jan", "age": 25}, 42, null]',
    }
    for file_name, content in broken_files.items():
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    random.seed(11)
    records = generate_valid_data(names, 10000)
    stats = corrupt_records(records, 0.2)
    print(stats)