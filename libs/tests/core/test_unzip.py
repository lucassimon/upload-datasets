import os
import pytest
import shutil


from apps.unzip import UnzipRepo


class TestUnzipRepo:

    def setup_method(self):
        self.from_here = os.path.dirname(__file__)
        relative_path = '../fixtures/archive.zip'
        zipfile_path = os.path.join(self.from_here, relative_path)
        unpack_path = '../unpack/archive/'

        self.unzip = UnzipRepo(zipfile_path, unpack_path)

    def teardown_method(self):
        self.unzip.close()

    def test_list_all_files(self):
        names = self.unzip.list_all_files()
        assert names == ['example.csv', 'boletos.csv']

    def test_extract_all(self):

        self.unzip.extract_all()
        unpack_path = '../../../unpack/archive/'
        checkdir = os.path.join(self.from_here, unpack_path)

        for filename in ['example.csv', 'boletos.csv']:
            assert os.path.exists(f'{checkdir}{filename}') is True

        shutil.rmtree(checkdir)
