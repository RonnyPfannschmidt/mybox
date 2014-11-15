import morepath
from mybox import App

#XXX: evil
if __name__ == '__main__':
    config = morepath.setup()
    config.scan()
    config.commit()
    morepath.run(App())
