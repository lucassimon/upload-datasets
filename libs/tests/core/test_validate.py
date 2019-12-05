import os
import pytest

from apps.validate import ImportDataset


class TestImportData:
    def setup_method(self):
        self.from_here = os.path.dirname(__file__)

    def factory_example(self):
        relative_path = "../fixtures/example.csv"
        dataset_path = os.path.join(self.from_here, relative_path)

        return ImportDataset(dataset_path, "example")

    def factory_boleto(self):
        relative_path = "../fixtures/boletos.csv"
        dataset_path = os.path.join(self.from_here, relative_path)

        return ImportDataset(dataset_path, "boleto")

    def factory_caers(self):
        relative_path = "../fixtures/CAERS_ASCII_2004_2017Q2.csv"
        dataset_path = os.path.join(self.from_here, relative_path)

        return ImportDataset(dataset_path, "caers")

    def test_return_errors_list_from_example_csv(self):
        validate_schema = self.factory_example()
        errors = validate_schema.validate()

        assert (
            str(errors[0])
            == '{row: 0, column: "Given Name"}: "Gerald " contains trailing whitespace'
        )
        assert (
            str(errors[1])
            == '{row: 1, column: "Age"}: "270" was not in the range [0, 120)'
        )
        assert (
            str(errors[2])
            == '{row: 1, column: "Sex"}: "male" is not in the list of legal options (Male, Female, Other)'
        )
        assert (
            str(errors[3])
            == '{row: 2, column: "Family Name"}: "Majewska " contains trailing whitespace'
        )
        assert (
            str(errors[4])
            == '{row: 2, column: "Customer ID"}: "775ANSID" does not match the pattern "\d{4}[A-Z]{4}"'
        )

    def test_return_errors_list_from_boleto_csv(self):
        validate_schema = self.factory_boleto()
        errors = validate_schema.validate()

        assert (
            str(errors[0])
            == '{row: 0, column: "status"}: "unavailable" is not in the list of legal options (pending, paid, due, error)'
        )

    def test_return_errors_list_from_caers_csv(self):
        validate_schema = self.factory_caers()
        errors = validate_schema.validate()

        assert len(errors) == 42792
