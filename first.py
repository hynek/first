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

It also supports the passing of a predicate whose result will be returned iff
the result is true:

>>> from first import first
>>> first([1, 1, 3, 4, 5], lambda x: (x ** 2) if (x % 2) == 0 else False)
16

:copyright: (c) 2012 by Hynek Schlawack.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'first'
__version__ = '1.0.0'
__author__ = 'Hynek Schlawack'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Hynek Schlawack'


def first(iterable, pred=None):
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

    If `pred` is specified, the result of `pred` is returned if the result is
    true.

    >>> first([1, 1, 3, 4, 5], lambda x: (x ** 2) if (x % 2) == 0 else False)
    16

    """
    if not pred:
        for el in iterable:
            if el:
                return el
    else:
        for el in iterable:
            rv = pred(el)
            if rv:
                return rv

    return None
