from more.static import StaticApp
import bowerstatic
from os.path import abspath, dirname, join

root = dirname(dirname(abspath(__file__)))
print root

bower = bowerstatic.Bower()
components = bower.components(
    'mybox', join(root, 'bower_components'))


class App(StaticApp):
    pass


@App.static_components()
def get_static():
    return components


@App.path(path='')
class Root(object):
    pass


@App.html(model=Root)
def hello(self, request):
    request.include('jquery')
    raise ValueError
    with open(join(root, 'static/index.html')) as fp:
        return fp.read()

