from more.static import StaticApp
import bowerstatic
from os.path import abspath, dirname, join

root = dirname(dirname(abspath(__file__)))
print root

bower = bowerstatic.Bower()
components = bower.components(
    'global', join(root, 'bower_components'))

local = bower.local_components('mybox', components)

local.component(root, version=None)


def jsx_script_tag(url):
    return '<script src="%s" type="text/jsx"></script>' % url

bower.renderer('.jsx', jsx_script_tag)


class App(StaticApp):
    pass


@App.static_components()
def get_static():
    return local


@App.path(path='')
class Root(object):
    pass


@App.html(model=Root)
def hello(self, request):
    request.include('es5-shim')
    request.include('react/react-with-addons.js')
    request.include('react/JSXTransformer.js')
    request.include('react-router')
    request.include('reflux')
    request.include('pure')
    request.include('MyBox/static/js/main.jsx')
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MyBox</title>
    </head>
    <body>
    <div>
        <h2>MyBox</h1>
        <p>
            Email Loading
        </p>
    </div>
    </body>
    </html>
    """
