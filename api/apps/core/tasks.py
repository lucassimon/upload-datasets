import os
from apps.celery import celery

from apps.validators.unzip import UnzipRepo
from apps.validators.validate import ImportDataset

from . import repositories


@celery.task()
def process(object_id, kind):
    repo = repositories.DatasetRepo()
    dataset = repo.by_id(object_id)

    zipfile_path = os.path.join(dataset.path, dataset.filename)
    unpack_path = dataset.path

    unzip = UnzipRepo(zipfile_path, unpack_path)
    unzip.extract_all()

    for filename in unzip.list_all_files():
        dataset_path = os.path.join(dataset.path, filename)
        import_dataset = ImportDataset(dataset_path, kind)
        import_dataset.pipeline(object_id)
