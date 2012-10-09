first: The function you always missed in Python
===============================================

*first* is a MIT licensed Python package with a simple function that returns
the first true value from an iterable, or ``None`` if there is none.  If you need
more power, you can also supply a predicate whose result will be returned `iff`_
true.

   I’m using the term “true” consistently with Python docs for ``any()`` and
   ``all()`` — it means that the value evaluates to true like: ``True``, ``1``,
   ``"foo"`` or ``[None]``. But **not**: ``None``, ``False`` or ``0``.  In
   JavaScript, they call this “truthy”.


Examples
========

A simple example first: ::

   >> from first import first
   >> first([0, None, False, [], (), 42])
   42

However, it’s especially useful for dealing with regular expressions in
``if/elif/else`` branches: ::

   import re

   from first import first


   re1 = re.compile('b(.*)')
   re2 = re.compile('a(.*)')

   m = first(regexp.match('abc') for regexp in [re1, re2])
   if not m:
      print('no match!')
   elif m.re is re1:
      print('re1', m.group(1))
   elif m.re is re2:
      print('re2', m.group(1))

The optional predicate gives you even *more* power. If you want to return the
square of the first even number from a list, just do the following: ::

   >>> from first import first
   >>> first([1, 1, 3, 4, 5], lambda x: (x ** 2) if (x % 2) == 0 else False)
   16


Usage
=====

The package consists of one module consisting of one function::

   from first import first

   first(iterable, pred=None)

This function returns the first element of ``iterable`` that is true if
``pred`` is ``None``. If there is no true element, ``None`` is returned.

If a callable is supplied in ``pred``, the result of ``pred(element)`` is
returned, if the result it true. 

*first* has no dependencies and should work with any Python available.  Of
course, it works with the awesome `Python 3`_ everybody should be using.


Background
==========

The idea for *first* goes back to a discussion I had with `Łukasz Langa`_ about
how the ``re`` example above is painful in Python.  We figured such a function
is missing Python, however it’s rather unlikely we’d get it in and even if, it
wouldn’t get in before 3.4 anyway, which is years away as of yours truly is
writing this.

So I decided to release it as a package for now.  If it proves popular enough,
it may even make it into Python’s stdlib in the end.


.. _`Python 3`: http://getpython3.com/
.. _`Łukasz Langa`: https://github.com/ambv
.. _`iff`: http://en.wikipedia.org/wiki/Iff

