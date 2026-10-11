from abc import ABC, abstractmethod


class SchemaField:
    def __init__(self, name, expected_type: type, required: bool):
        """Definition of a single field in a schema.

        Args:
            name (_type_): _description_
            expected_type (type): _description_
            required (bool): _description_
        """
        self.name = name
        self.expectedType = expected_type
        self.requiered = required

class Schema:
    def __init__(self, SchemaFields: list[SchemaField]):
        """Collection(list) of schema fields.

        Args:
            SchemaFields (list[SchemaField]): _description_
        """
        self.SchemaFields = SchemaFields

class ValidationResult:
    def __init__(self, is_valid: bool, errors: list[str]):
        """Result of validating a record against a schema.

        Args:
            is_valid (bool): _description_
            errors (list[str]): _description_
        """
        self.is_valid = is_valid
        self.erros = errors

class SchemaValidator(ABC):
    def __init__(self, Schema):
        """Base class for validating records against a schema.
        
        Args:
            Schema (_type_): _description_
        """
        self.Schema = Schema

    @abstractmethod
    def validate(record: dict) -> ValidationResult:
        """Validate record against the schema.

        Args:
            record (dict): _description_

        Returns:
            ValidationResult: _description_
        """
        pass