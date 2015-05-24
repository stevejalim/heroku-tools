# -*- coding: utf-8 -*-
"""Package setup for heroku-tools CLI application."""
import os

from setuptools import setup

dependencies = ['click', 'envoy', 'pyyaml', 'requests']

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='heroku-tools',
    version='0.1.3',
    url='https://github.com/yunojuno/heroku-tools',
    license='MIT',
    author='Hugo Rodger-Brown',
    author_email='hugo@yunojuno.com',
    description=(
        "Command line application for managing Heroku applications."
    ),
    long_description=README,
    include_package_data=True,
    packages=[
        'heroku_tools',
    ],
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'deploy = heroku_tools.deploy:deploy',
            'config = heroku_tools.deploy:config',
            'migrate = heroku_tools.deploy:migrate'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ]
)
