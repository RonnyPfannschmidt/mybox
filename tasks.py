from invoke import Collection, task, run as base_run
from functools import partial

run = partial(base_run, echo=True)


fetches = {
    'js/ember.js': 'http://builds.emberjs.com/release/ember.js',
    'js/handlebars.js': 'http://builds.handlebarsjs.com'
                        '.s3.amazonaws.com/handlebars-v1.3.0.js',
    'css/pure.css': 'http://yui.yahooapis.com/pure/0.5.0/pure-min.css',
}


@task
def fetch_deps():
    run('mkdir -p static/{css,js}')
    for target, source in fetches.items():
        run('wget {} -O static/{}'.format(source, target))


@task(default=True)
def refresh_env():
    run('pip install -U -r requirements.txt')


@task
def check():
    run('flake8 --max-complexity 8 *.py mybox testing')


@task
def test():
    run('py.test')


@task
def serve():
    run('python -m mybox')

ns = Collection(
    fetch_deps,
    refresh_env,
    check,
    serve,
    test,
)
