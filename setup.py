from setuptools import setup, find_packages

setup(
    name='mybox',
    description='web ui for your Maildir++',
    get_version_from_scm=True,
    packages=find_packages(),
    setup_requires=[
        'hgdistver',
    ],
    requires=[
        'livereload'
    ]
)
