# Python

# Third
from mongoengine.errors import NotUniqueError, ValidationError

# Apps

# Local
from .models import Dataset, Log
from apps.responses import Response


class DatasetRepo:
    def __init__(self):
        self.model = Dataset
        self.resource = "Dataset"
        self.response = Response(self.resource)

    def create(self, data: dict):
        try:
            return self.model(**data).save()

        except NotUniqueError as e:
            raise e

        except ValidationError as e:
            raise e

        except Exception as e:
            raise e

    def by_id(self, object_id):
        try:
            return self.model.objects.get(id=object_id)

        except Exception as e:
            return self.response.exception(description=e.__str__())

    def by_criteria(
        self, criteria: dict, order: str = "created", items: int = None, status=None
    ):
        try:
            if status:
                dataset = self.model.objects(status, **criteria).order_by(order)
            else:
                dataset = self.model.objects(**criteria).order_by(order)
            if items:
                return dataset[:items]

            return dataset

        except Exception as e:
            return self.response.exception(description=e.__str__())

    def paginate(self, criteria: dict, page, per_page, order: str = "created"):
        try:
            return (
                self.model.objects(**criteria).order_by(order).paginate(page, per_page)
            )

        except Exception as e:
            raise e


class LogRepo:
    def __init__(self):
        self.model = Log
        self.resource = "Log"
        self.response = Response(self.resource)

    def create(self, data: dict):
        try:
            return self.model(**data).save()

        except NotUniqueError as e:
            raise e

        except ValidationError as e:
            raise e

        except Exception as e:
            raise e

    def insert(self, logs: list):
        """Bulk create"""
        try:
            return self.model.objects.insert(logs)

        except NotUniqueError as e:
            raise e

        except ValidationError as e:
            raise e

        except Exception as e:
            raise e

    def by_criteria(
        self, criteria: dict, order: str = "created", items: int = None, status=None
    ):
        try:
            if status:
                log = self.model.objects(status, **criteria).order_by(order)
            else:
                log = self.model.objects(**criteria).order_by(order)
            if items:
                return log[:items]

            return log

        except Exception as e:
            return self.response.exception(description=e.__str__())
