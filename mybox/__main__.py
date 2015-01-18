import sys
import morepath
from werkzeug import serving
import more.static
import mybox
from mybox.app import Main

if __name__ == '__main__':
    config = morepath.setup()
    config.scan(mybox.app)
    config.scan(more.static)
    config.commit()
    app = Main(sys.argv[1])
    serving.run_simple(
        'localhost', 5000, app,
        use_debugger=True, use_reloader=True)
