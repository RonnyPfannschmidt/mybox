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
    request.include('react')
    request.include('react/JSXTransformer.js')
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
    <div id="startpoint">
        <h2>MyBox</h1>
        <p>
            Email Loading
        </p>
    </div>
    <script type="text/jsx">
    var startpoint = document.getElementById('startpoint');
    React.render(
        <div id="startpoint">
          <h2>MyBox Startup</h2>
          <p> Email starting</p>
        </div>
        , startpoint);
    MyBox.startup(startpoint);
    </script>
    </body>
    </html>
    """

