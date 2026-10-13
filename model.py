from abc import ABC, abstractmethod

class SchemaField:
    def __init__(self, name: int, expected_type: type, required: bool):
        """Definition of a single field in a schema.

        Args:
            name (_type_): _description_
            expected_type (type): _description_
            required (bool): _description_
        """
        self.name = name
        self.expected_type = expected_type
        self.required = required

class Schema:
    def __init__(self, schema_fields: list[SchemaField]):
        """Collection(list) of schema fields.

        Args:
            SchemaFields (list[SchemaField]): _description_
        """
        self.schema_fields = schema_fields

class ValidationResult:
    def __init__(self, is_valid: bool, errors: list[str]):
        """Result of validating a record against a schema.

        Args:
            is_valid (bool): _description_
            errors (list[str]): _description_
        """
        self.is_valid = is_valid
        self.errors = errors

class SchemaValidator(ABC):
    def __init__(self, schema: Schema):
        """Base class for validating records against a schema.
        
        Args:
            Schema (_type_): _description_
        """
        self.schema = schema

    @abstractmethod
    def validate(self, record: dict) -> ValidationResult:
        """Validate record against the schema.

        Args:
            record (dict): _description_

        Returns:
            ValidationResult: _description_
        """
        pass

class CoercingValidator(SchemaValidator):
    def validate(self, record: dict) -> ValidationResult:
        for field in self.schema.schema_fields:
            if field.name in record:
                if field.expected_type != type(record[field.name]):
                    try:
                        converted_val = field.expected_type(record[field.name])
                    except:
                        error_msg = f'Value type does not match for key: {field.name}, type {type(record[field.name])}, expected: {field.expected_type}'
                        return ValidationResult(False, [error_msg])
            else :
                if field.required:
                    error_msg = f'Record keys does not match, no {field.name} in {record}'
                    return ValidationResult(False, [error_msg])
        return ValidationResult(True, [])
            


        
                
