from morepath import App


class MailBox(App):
    def __init__(self, backend):
        self.backend = backend


@MailBox.path('')
def Root(object):
    def __init__(self, app):
        self.backed = app.backend



