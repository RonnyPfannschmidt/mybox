

from tornado.web import StaticFileHandler
from livereload.server import BaseServer


from mybox.web import APIHandler


def F(match, **opts):
    return (match, StaticFileHandler, opts)


class MyBoxServer(BaseServer):
    def get_web_handlers(self):
        return [
            F('/jspm_packages/(config\.js)', path='.',),
            F('/jspm_packages/(.*)', path='jspm_packages'),
            F('/lib/(.*)', path='app'),
            ('api/(.*)', APIHandler, {'backend': None}),
            F('.*()', path='app/html', default_filename='index.html'),
        ]


if __name__ == '__main__':
    server = MyBoxServer()
    server.watch('jspm_packages')
    server.watch('app')
    server.serve(port=5050)
