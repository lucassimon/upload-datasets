import pytest
from unittest import mock

from apps.core.models import Dataset, Log
from .factories import DatasetFactory, LogFactory
from tests.utils import replace_id_to_take_snapshot


class TestLog:
    def setup_method(self):
        DatasetFactory.reset_sequence()
        LogFactory.reset_sequence()

    def teardown_method(self):
        Dataset.objects.delete()
        Log.objects.delete()

    def make_request(self, client, dataset_id):
        url = f"/logs/{dataset_id}"
        return client.get(url, content_type="application/json")

    def test_should_response_logs(self, auth, mongo, snapshot):
        dataset = DatasetFactory.create(id="5dec15573a07786542aba227")
        dataset_id = f"{dataset.id}"
        LogFactory.create_batch(4, dataset_id=dataset_id)
        response = self.make_request(auth, dataset_id)
        assert response.status_code == 200
        res = response.json
        items = replace_id_to_take_snapshot(response.json.get("data"))
        res["data"] = items
        snapshot.assert_match(res)

    @mock.patch("apps.core.repositories.Log.objects")
    def test_should_response_exception_when_an_error_raised(
        self, DatasetMock, auth, mongo
    ):
        DatasetMock.side_effect = Exception("Some error occurred")
        response = self.make_request(auth, "fake_id")
        assert response.status_code == 500
        assert response.json.get("description") == "Some error occurred"
