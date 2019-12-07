import pandas as pd

from apps.core.models import Log
from apps.core.repositories import LogRepo
from . import schemas


class ImportDataset:
    def __init__(self, dataset_path, kind):
        self.dataset_path = dataset_path
        self.dataset = pd.read_csv(self.dataset_path)

        self.kind = kind
        self.schema = {
            "example": schemas.CsvExampleSchema(),
            "boleto": schemas.CsvBoletoSchema(),
            "caers": schemas.CsvCaersSchema(),
        }

    def remove_duplicated(self):
        """
        Remove duplicated items on csv with pandas
        """
        self.dataset.drop_duplicates(keep=False, inplace=True)

    def validate(self):
        errors = self.schema[self.kind].schemas.validate(self.dataset)
        return errors

    def log_errors(self, uploaded_id, errors):
        """
        Save errors on database
        """
        # TODO save all errors with batch flow
        logs = [
            Log(
                dataset_id=uploaded_id,
                row=i.row,
                value=i.value,
                column=i.column,
                message=i.message,
            )
            for i in errors
        ]

        try:
            repo = LogRepo()
            repo.insert(logs)

        except Exception as e:
            raise e

    def extract(self):
        """
        Extract each row and transform data
        """
        # TODO It can be send to SQS or RabbitMQ or Kafka as a json message
        # then a worker like kombu or golang transform data and save it
        pass

    def load(self):
        """
        Save each row on database
        """
        # TODO If not send to Queue then save it
        pass

    def pipeline(self, uploaded_id):
        self.remove_duplicated()
        errors = self.validate()

        if errors:

            try:
                self.log_errors(uploaded_id, errors)
            except Exception as e:
                raise e

            errors_count = len(errors)
            # TODO Create a Custom exception?
            raise ValueError(f"There are {errors_count} errors")

        self.extract()
        self.load()
