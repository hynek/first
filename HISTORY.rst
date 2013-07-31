History
-------

2.1.0 (unrelease)
+++++++++++++++++
   - *Backward incompatible*: Drop support for Python older than 2.6.
   - Make installable on systems that don’t support UTF-8 by default.


2.0.0 (2012-10-13)
++++++++++++++++++
   - `pred` proved to be rather useless.  Changed to `key` which is just
     a selector.  This is a *backward incompatible* change and the reason for
     going 2.0.
   - Add `default` argument which is returned instead of `None` if no true
     element is found.

1.0.2 (2012-10-09)
++++++++++++++++++
   - Fix packaging. I get this never right the first time. :-/

1.0.1 (2012-10-09)
++++++++++++++++++
   - Documentation fixes only.

1.0.0 (2012-10-09)
++++++++++++++++++
   - Initial release.
