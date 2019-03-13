try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'project description',
    'author': 'project author',
    'url': 'project url',
    'download url': 'project download url',
    'author email': 'project author email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'project name'

}