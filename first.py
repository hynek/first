## -*- coding: utf-8 -*-

"""
first
=====

first is the function you always missed in Python.

In the simplest case, it returns the first true element from an iterable:

>>> from first import first
>>> first([0, False, None, [], (), 42])
42

Or None if there is none:

>>> from first import first
>>> first([]) is None
True
>>> first([0, False, None, [], ()]) is None
True

It also supports the passing of a key argument to help selecting the first
match in a more advanced way.

>>> from first import first
>>> first([1, 1, 3, 4, 5], lambda x: x % 2 == 0)
4

:copyright: (c) 2012 by Hynek Schlawack.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'first'
__version__ = '1.0.2'
__author__ = 'Hynek Schlawack'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Hynek Schlawack'


def first(iterable, key=None, default=None):
    """
    Return first element of `iterable` that evaluates true, else return None.

    >>> first([0, False, None, [], (), 42])
    42

    >>> import re
    >>> m = first(re.match(regex, 'abc') for regex in ['b.*', 'a(.*)'])
    >>> m.group(1)
    'bc'

    >>> first([]) is None
    True
    >>> first([0, False, None, [], ()]) is None
    True

    If `key` is specified, the result of `key` is returned if the result is
    true.

    >>> first([1, 1, 3, 4, 5], lambda x: x % 2 == 0)
    4

    """
    if key is None:
        for el in iterable:
            if el:
                return el
    else:
        for el in iterable:
            if key(el):
                return el

    return default
