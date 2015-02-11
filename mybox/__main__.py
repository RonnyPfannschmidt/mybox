import sys

from tornado.web import StaticFileHandler, Application
from livereload.server import BaseServer
from tornado.ioloop import IOLoop

from mybox.web import APIHandler


def F(match, **opts):
    return (match, MyStaticFileHandler, opts)


class MyStaticFileHandler(StaticFileHandler):
    def set_extra_headers(self, path):
        # Disable cache
        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')


class ShellHandler(MyStaticFileHandler):
    def get(self, include_body=True):
        super(ShellHandler, self).get('index.html', include_body)


handlers = [
    F('/jspm_packages/(.*)', path='jspm_packages'),
    F('/(\w+\.js.*)', path='.',),
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
