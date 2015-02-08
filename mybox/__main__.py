import sys

from tornado.web import StaticFileHandler, Application
from livereload.server import BaseServer
from tornado.ioloop import IOLoop

from mybox.web import APIHandler


def F(match, **opts):
    return (match, StaticFileHandler, opts)


class ShellHandler(StaticFileHandler):
    def get(self, include_body=True):
        super(ShellHandler, self).get('index.html', include_body)


handlers = [
    F('/jspm_packages/(config\.js)', path='.',),
    F('/jspm_packages/(.*)', path='jspm_packages'),
    F('/(?:lib|my-box)/(.*)', path='lib'),
    ('api/(.*)', APIHandler, {'backend': None}),
    ('/.*', ShellHandler, {'path': 'lib/html'}),
]


class MyBoxServer(BaseServer):
    def get_web_handlers(self):
        return handlers


if __name__ == '__main__':
    if 'live' in sys.argv:
        server = MyBoxServer()
        server.watch('jspm_packages')
        server.watch('app')
        server.serve(port=5050)
    else:
        app = Application(handlers)
        app.listen(5000)
        IOLoop.instance().start()
