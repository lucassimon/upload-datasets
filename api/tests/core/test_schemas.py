import pytest
from marshmallow.fields import Integer, Str, Date

from apps.core.schemas import (
    CommonDataSet,
    ListDataSetSchema,
    DetailDataSetSchema,
    ListLogSchema,
)


class TestCommonDataSet:
    def setup_method(self):
        self.payload = {}
        self.schema = CommonDataSet()
        self.data, self.errors = self.schema.load(self.payload)

    def test_id_is_str_field(self):
        assert isinstance(CommonDataSet._declared_fields.get("id"), Str) is True

    def test_filename_is_str_field(self):
        assert isinstance(CommonDataSet._declared_fields.get("filename"), Str) is True

    def test_path_is_str_field(self):
        assert isinstance(CommonDataSet._declared_fields.get("path"), Str) is True

    def test_status_is_str_field(self):
        assert isinstance(CommonDataSet._declared_fields.get("status"), Str) is True


class TestListDataSetSchema:
    def setup_method(self):
        self.payload = {}
        self.schema = ListDataSetSchema()
        self.data, self.errors = self.schema.load(self.payload)

    def test_id_is_str_field(self):
        assert isinstance(ListDataSetSchema._declared_fields.get("id"), Str) is True

    def test_filename_is_str_field(self):
        assert (
            isinstance(ListDataSetSchema._declared_fields.get("filename"), Str) is True
        )

    def test_path_is_str_field(self):
        assert isinstance(ListDataSetSchema._declared_fields.get("path"), Str) is True

    def test_status_is_str_field(self):
        assert isinstance(ListDataSetSchema._declared_fields.get("status"), Str) is True


class TestDetailDataSetSchema:
    def setup_method(self):
        self.payload = {}
        self.schema = DetailDataSetSchema()
        self.data, self.errors = self.schema.load(self.payload)

    def test_id_is_str_field(self):
        assert isinstance(DetailDataSetSchema._declared_fields.get("id"), Str) is True

    def test_filename_is_str_field(self):
        assert (
            isinstance(DetailDataSetSchema._declared_fields.get("filename"), Str)
            is True
        )

    def test_path_is_str_field(self):
        assert isinstance(DetailDataSetSchema._declared_fields.get("path"), Str) is True

    def test_status_is_str_field(self):
        assert (
            isinstance(DetailDataSetSchema._declared_fields.get("status"), Str) is True
        )


class TestListLogSchema:
    def setup_method(self):
        self.payload = {}
        self.schema = ListLogSchema()
        self.data, self.errors = self.schema.load(self.payload)

    def test_id_is_str_field(self):
        assert isinstance(ListLogSchema._declared_fields.get("id"), Str) is True

    def test_dataset_id_is_str_field(self):
        assert isinstance(ListLogSchema._declared_fields.get("dataset_id"), Str) is True

    def test_row_is_str_field(self):
        assert isinstance(ListLogSchema._declared_fields.get("row"), Str) is True

    def test_column_is_str_field(self):
        assert isinstance(ListLogSchema._declared_fields.get("column"), Str) is True

    def test_message_is_str_field(self):
        assert isinstance(ListLogSchema._declared_fields.get("message"), Str) is True

    def test_value_is_str_field(self):
        assert isinstance(ListLogSchema._declared_fields.get("value"), Str) is True
