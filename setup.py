
try:
    from setuptools import setup
except ImportError:
    print "Falling back to distutils. Functionality may be limited."
    from distutils.core import setup

config = {
    'description'  : 'A script for downloading imgur.com urls with their metadata',
    'author'       : 'Brandon Sandrowicz',
    'url'          : 'http://github.com/bsandrow/imgur-get',
    'author_email' : 'brandon@sandrowicz.org',
    'version'      : '1.0',
    'packages'     : [],
    'scripts'      : ['imgur-get'],
    'name'         : 'imgur-get',
}

setup(**config)
