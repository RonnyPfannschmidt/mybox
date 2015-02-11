import os


ELEMENTS = 'tmp', 'cur', 'new'


def map_maildir_name(name):
    return ''

def list_maildirs(path):
    items = os.listdir(path)

    res = [
        x for x in items
        if len(x) > 2 and x[0] == '.' and x[1] != '.'
    ]

    if all(x in items for x in ELEMENTS):
        res.append('inbox')
    return res


class Backend(object):
    def __init__(self, path):
        self.path = path

    @classmethod
    def create(cls, path):
        return cls(str(path))

    def tree(self):
        try:
            items = list_maildirs(self.path)
            return dict.fromkeys(items)
        except IOError:
            return {}

    def add_folder(self, name):
        dirname = map_maildir_name(name)
        os.mkdir(os.path.join(self.path, dirname))
        for item in ELEMENTS:
            os.mkdir(os.path.join(self.path, dirname, item))
