from invoke import Collection, task, run as base_run
from functools import partial

run = partial(base_run, echo=True)


@task
def fetch_deps():
    run('mkdir -p static/css')
    run('wget https://raw.githubusercontent.com/'
        'picnicss/picnic/master/releases/latest.css -O static/css/picnic.css')


@task(default=True)
def refresh_env():
    run('pip install -U -r requirements.txt')


@task
def check():
    run('flake8 --max-complexity 8 *.py mybox testing')


@task
def test():
    run('py.test')


ns = Collection(
    fetch_deps,
    refresh_env,
    check,
    test,
)
