from setuptools import setup, find_packages

setup(
    name='mybox',
    description='web ui for your Maildir++',
    get_version_from_scm=True,
    setup_requires=[
        'hgdistver',
    ],
    requires=[
        'livereload'
    ]
)
