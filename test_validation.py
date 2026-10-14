from model import Schema, SchemaField, CoercingValidator

schema = Schema([
    SchemaField("name", str, True),
    SchemaField("age", int, True),
    SchemaField("email", str, False),
])
validator = CoercingValidator(schema)


# (a) fully valid record passes without errors
def test_valid_record_passes():
    result = validator.validate({"name": "Jan", "age": 25, "email": "jan@email.com"})
    assert result.is_valid
    assert result.errors == []


# (b) missing required field reports an error with its name
def test_missing_required_field_reports_its_name():
    result = validator.validate({"name": "Jan", "email": "jan@email.com"})
    assert not result.is_valid
    assert "no age" in result.errors[0]


# (c) wrong but convertible type is coerced, so the record passes
def test_convertible_type_is_coerced():
    result = validator.validate({"name": "Jan", "age": "25"})
    assert result.is_valid
    assert result.errors == []


# (d) variant C: value that cannot be converted is an error
def test_non_convertible_type_fails():
    result = validator.validate({"name": "Jan", "age": "abc"})
    assert not result.is_valid
    assert "age" in result.errors[0]


# (d) variant C: validation stops at the first error, so only one message
def test_two_errors_return_one_message():
    result = validator.validate({"age": "abc"})
    assert not result.is_valid
    assert len(result.errors) == 1
