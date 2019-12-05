# Python

# Third
from mongoengine.errors import NotUniqueError, ValidationError

# Apps

# Local
from .models import Dataset


class DatasetRepo:
    def __init__(self):
        self.model = Dataset
        self.resource = "Dataset"

    def create(self, data: dict):
        try:
            return self.model(**data).save()
        except NotUniqueError as e:
            raise e
        except ValidationError as e:
            raise e
        except Exception as e:
            raise e
