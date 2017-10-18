from setuptools import setup

import first
import sys


if sys.version_info[0] >= 3:
    openf = open
else:
    import codecs
    openf = codecs.open

def read(fn):
    with openf(fn, encoding='utf-8') as fp:
        return fp.read()


setup(
    name='first',
    version=first.__version__,
    description='Return the first true value of an iterable.',
    long_description=(read('README.rst') + '\n\n' +
                      read('HISTORY.rst') + '\n\n' +
                      read('AUTHORS.rst')),
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
