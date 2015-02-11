

class Backend(object):
    def __init__(self, folders):
        self.folders = folders

    @classmethod
    def create(cls, folders):
        return cls(folders)

    def tree(self):
        return self.folders

    def add_folder(self, name):
        self.folders[name] = {}
