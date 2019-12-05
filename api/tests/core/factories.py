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
