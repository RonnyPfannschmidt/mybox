import morepath
from werkzeug import serving

import mybox


#XXX: evil
if __name__ == '__main__':
    config = morepath.setup()
    config.scan(mybox)
    config.commit()
    serving.run_simple('localhost', 5000, mybox.App(),
                       use_debugger=True, use_reloader=True)
