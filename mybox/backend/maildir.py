import os


ELEMENTS = 'tmp', 'cur', 'new'


def map_maildir_name(name):
    return ''


class Backend(object):
    def __init__(self, path):
        self.path = path

    @classmethod
    def create(cls, path):
        return cls(str(path))

    def tree(self):
        try:
            items = os.listdir(self.path)
            return dict.fromkeys(items)
        except IOError:
            return {}

    def add_folder(self, name):
        dirname = map_maildir_name(name)
        os.mkdir(os.path.join(self.path, dirname))
        for item in ELEMENTS:
            os.mkdir(os.path.join(self.path, dirname, item))
