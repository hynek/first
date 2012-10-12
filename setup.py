from setuptools import setup

import first


setup(
    name='first',
    version=first.__version__,
    description='Return the first true value of an iterable.',
    long_description=(open('README.rst').read() + '\n\n' +
                      open('HISTORY.rst').read() + '\n\n' +
                      open('AUTHORS.rst').read()),
    url='http://github.com/hynek/first/',
    license=first.__license__,
    author=first.__author__,
    author_email='hs@ox.cx',
    py_modules=['first'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
