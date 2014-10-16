
from invoke import task, run


@task()
def fetch_deps():
    run('mkdir -p static/css')
    run('wget https://raw.githubusercontent.com/'
        'picnicss/picnic/master/releases/latest.css -O static/css/picnic.css')


