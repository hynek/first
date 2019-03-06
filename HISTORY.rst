.. :changelog:

History
-------

2.0.2 (2019-03-06)
++++++++++++++++++

- Package tests as part of the dist.
- Update docs.
- Drop unsupported Python versions from CI.
  N.B. The code hasn't changed and ``first`` continues to work as before.


2.0.1 (2013-08-04)
++++++++++++++++++

- Make installable on systems that don’t support UTF-8 by default.
- *Backward incompatible*: Drop support for Python older than 2.6, the previous fix gets too convoluted otherwise.
  Please don’t use Python < 2.6 anyway.
  I beg you.
  N.B. that this is a *pure packaging/QA matter*: the module still works perfectly with ancient Python versions.


2.0.0 (2012-10-13)
++++++++++++++++++

- `pred` proved to be rather useless.  Changed to `key` which is just a selector.  This is a *backward incompatible* change and the reason for going 2.0.
- Add `default` argument which is returned instead of `None` if no true element is found.

1.0.2 (2012-10-09)
++++++++++++++++++

- Fix packaging. I get this never right the first time. :-/

1.0.1 (2012-10-09)
++++++++++++++++++

- Documentation fixes only.

1.0.0 (2012-10-09)
++++++++++++++++++

- Initial release.
