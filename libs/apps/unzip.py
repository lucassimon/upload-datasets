import zipfile


class UnzipRepo:

    def __init__(self, zipfile_path, unpack_path):
        self.zipfile_path = zipfile_path
        self.unpack_path = unpack_path
        self.filenames = []

        try:
            self.zipped_file = zipfile.ZipFile(self.zipfile_path, 'r')

        except zipfile.BadZipfile as e:
            raise e

        except Exception as e:
            raise e

    def list_all_files(self):
        names = self.zipped_file.namelist()
        self.filenames.extend(names)
        return names

    def extract_file(self, filename):
        try:
            self.zipped_file.extract(filename, self.unpack_path)
        except Exception as e:
            raise e

    def extract_all(self):
        try:
            self.zipped_file.extractall(self.unpack_path)
        except Exception as e:
            raise e

    def close(self):
        self.zipped_file.close()
