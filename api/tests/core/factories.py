import factory

from apps.core.models import Dataset, Log
from apps.core.choices import INITIAL


class DatasetFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Dataset

    filename = factory.Sequence(lambda n: "Filename %d" % n)
    path = "/path/to/uploaded"
    status = INITIAL


class LogFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Log

    dataset_id = "5ce089d4fb5d1b3bd3ad96a2"
    row = 0
    column = "status"
    message = "this column does not accepts unvailable in status"
    value = "unavailable"
