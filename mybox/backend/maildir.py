import os
import re


INBOX_FOLDER = 'INBOX'
INBOX_NAME = ''
SEP = '/'
MAILDIR_ELEMENTS = frozenset(['tmp', 'cur', 'new'])
MAILDIR_FOLDER_REGEX = re.compile('\.[^\.].*')


def folder_to_maildir(folder):
    if folder == INBOX_FOLDER:
        return INBOX_NAME
    else:
        return '.' + '.'.join(folder.split(SEP))


def maildir_to_folder(name):
    if name == INBOX_NAME:
        return INBOX_FOLDER
    else:
        return SEP.join(name.split('.')[1:])


def list_maildirs(path):
    items = os.listdir(path)
    res = list(filter(MAILDIR_FOLDER_REGEX.match, items))
    if MAILDIR_ELEMENTS.issubset(items):
        res.append(INBOX_NAME)
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
            return dict.fromkeys(map(maildir_to_folder, items))
        except IOError:
            return {}

    def add_folder(self, name):
        dirname = folder_to_maildir(name)
        os.mkdir(os.path.join(self.path, dirname))
        for item in MAILDIR_ELEMENTS:
            os.mkdir(os.path.join(self.path, dirname, item))
