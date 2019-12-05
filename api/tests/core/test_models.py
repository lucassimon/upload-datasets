from datetime import datetime

# Third
import pytest
from mongoengine import StringField, IntField, BooleanField, DateField, DateTimeField

from apps.core.models import Dataset
from apps.core.choices import INITIAL


class TestDataset:
    def setup_method(self):
        self.data = {}
        self.model = Dataset(**self.data)

    def test_filename_field_exists(self):
        assert "filename" in self.model._fields
        assert isinstance(self.model._fields["filename"], StringField)
        assert self.model._fields["filename"].required is True

    def test_path_field_exists(self):
        assert "path" in self.model._fields
        assert isinstance(self.model._fields["path"], StringField)
        assert self.model._fields["path"].required is True

    def test_status_field_exists(self):
        assert "status" in self.model._fields
        assert isinstance(self.model._fields["status"], StringField)
        assert self.model._fields["status"].required is True
        assert self.model._fields["status"].default is INITIAL

    def test_created_field_exists(self):
        assert "created" in self.model._fields
        assert isinstance(self.model._fields["created"], DateTimeField)

    def test_updated_field_exists(self):
        assert "updated" in self.model._fields
        assert isinstance(self.model._fields["updated"], DateTimeField)
