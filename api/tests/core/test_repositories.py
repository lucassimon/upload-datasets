import pytest
from unittest import mock


from apps.core.repositories import DatasetRepo
from apps.core.models import Dataset
from .factories import DatasetFactory


class TestDatasetRepo:
    def setup_method(self):
        DatasetFactory.reset_sequence()

    def teardown_method(self):
        Dataset.objects.delete()

    def test_should_return_account(self, mongo):
        dataset = DatasetFactory.create()
        instance = DatasetRepo().by_id(f"{dataset.id}")
        assert isinstance(instance, Dataset) is True

    @mock.patch("apps.core.repositories.Dataset.objects")
    def test_should_response_exception_when_an_error_raised(self, DatasetMock):
        DatasetMock.get.side_effect = Exception("Some error occurred")
        response = DatasetRepo().by_id("fake-account-id")
        assert response.status_code == 500
        assert response.json.get("description") == "Some error occurred"
