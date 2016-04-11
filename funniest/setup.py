try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
	'description': 'Funny Joke',
	'author': 'Tucker Rosebrock',
	'url': 'https://github.com/tuckyeah/',
	'author_email': 'h.rosebrock@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['funniest'],
	'scripts': ['bin/funniest-joke'],
	'name': 'funniest joke'
}

setup(**config)