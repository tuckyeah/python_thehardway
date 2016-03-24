try: 
    from setuptools import setup 
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Windows Beta Project',
    'author': 'Tucker Rosebrock',
    'url': 'https://github.com/tuckyeah',
    'download_url': 'https://github.com/tuckyeah',
    'author_email': 'h.rosebrock@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['BETA'],
    'scripts': [],
    'name': 'work_beta'
}

setup(**config)