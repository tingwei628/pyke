import os
from setuptools import setup

required=[
    'Flask',
    'gunicorn',
    'beautifulsoup4',
    'requests-html',
    'pyppeteer'
]

#with open('requirements.txt') as f:
#    required = f.read().splitlines()
    
setup(
    install_requires=required
)
