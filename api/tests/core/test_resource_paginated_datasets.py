import pytest
from unittest import mock

from apps.core.models import Dataset
from .factories import DatasetFactory
from tests.utils import replace_id_to_take_snapshot


class TestDataset:
    def setup_method(self):
        DatasetFactory.reset_sequence()

    def teardown_method(self):
        Dataset.objects.delete()

    def make_request(self, client, query=None):
        url = "/datasets/page/1"
        return client.get(url, content_type="application/json")

    def test_should_response_dataset_paginated(self, auth, mongo, snapshot):
        DatasetFactory.create_batch(3)
        response = self.make_request(auth)
        assert response.status_code == 200
        res = response.json
        items = replace_id_to_take_snapshot(response.json.get("data"))
        res["data"] = items
        snapshot.assert_match(res)

    @mock.patch("apps.core.repositories.Dataset.objects")
    def test_should_response_exception_when_an_error_raised(
        self, DatasetMock, auth, mongo
    ):
        DatasetMock.side_effect = Exception("Some error occurred")
        response = self.make_request(auth)
        assert response.status_code == 500
        assert response.json.get("description") == "Some error occurred"
