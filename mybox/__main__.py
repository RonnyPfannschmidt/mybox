import morepath
from werkzeug import serving
import more.static
import mybox
from mybox.app import App

if __name__ == '__main__':
    config = morepath.setup()
    config.scan(mybox.app)
    config.scan(more.static)
    config.commit()
    serving.run_simple(
        'localhost', 5000, App(),
        use_debugger=True, use_reloader=True)
