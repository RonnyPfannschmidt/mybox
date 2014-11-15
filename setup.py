from setuptools import setup

setup(
    name='mybox',
    description='web ui for your Maildir++',
    get_version_from_scm=True,
    setup_requires=[
        'hgdistver',
    ],
    requires=[
        'more.static',
        'werkzeug',
    ]
)