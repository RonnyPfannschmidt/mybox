from more.static import StaticApp


class App(StaticApp):
    pass


@App.path(path='')
class Root(object):
    pass


@App.view(model=Root)
def root(self, request):
    return ''
