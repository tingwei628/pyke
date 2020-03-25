import os
from setuptools import setup
from setuptools.command.install import install

class PostInstallCommand(install):
    
    def run(self):
        install.run(self)
        os.system('pyppeteer-install')


with open('requirements.txt') as f:
    required = f.read().splitlines()
    
setup(
    install_requires=required,
    cmdclass={
        'install': PostInstallCommand
    }
)
