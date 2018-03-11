SqueezeBox integration for Beets
================================

 |Travis CI|  |Coveralls|  |GitHub Issues|  |License|
 |Latest Version|  |Downloads|

A Beets plugin to integrate it with the SqueezeBox eco-system.

.. contents:: **Contents**


.. _setup-start:

Introduction
------------

**TODO**


Usage
-----

**TODO**


Installation
------------

*SqueezeBox integration for Beets* can be installed via ``pip install beetzbox`` as usual,
see `releases <https://github.com/jhermann/beetzbox/releases>`_ for an overview of available versions.
To get a bleeding-edge version from source, use these commands::

    repo="jhermann/beetzbox"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"

As a developer, to create a working directory for this project, call these commands::

    git clone "https://github.com/jhermann/beetzbox.git"
    cd "beetzbox"
    command . .env --yes --develop  # add '--virtualenv /usr/bin/virtualenv' for Python2
    invoke build check

You might also need to follow some
`setup procedures <https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup>`_
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.


.. |Travis CI| image:: https://api.travis-ci.org/jhermann/beetzbox.svg
    :target: https://travis-ci.org/jhermann/beetzbox
.. |Coveralls| image:: https://img.shields.io/coveralls/jhermann/beetzbox.svg
    :target: https://coveralls.io/r/jhermann/beetzbox
.. |GitHub Issues| image:: https://img.shields.io/github/issues/jhermann/beetzbox.svg
    :target: https://github.com/jhermann/beetzbox/issues
.. |License| image:: https://img.shields.io/pypi/l/beetzbox.svg
    :target: https://github.com/jhermann/beetzbox/blob/master/LICENSE
.. |Development Status| image:: https://pypip.in/status/beetzbox/badge.svg
    :target: https://pypi.python.org/pypi/beetzbox/
.. |Latest Version| image:: https://img.shields.io/pypi/v/beetzbox.svg
    :target: https://pypi.python.org/pypi/beetzbox/
.. |Download format| image:: https://pypip.in/format/beetzbox/badge.svg
    :target: https://pypi.python.org/pypi/beetzbox/
.. |Downloads| image:: https://img.shields.io/pypi/dw/beetzbox.svg
    :target: https://pypi.python.org/pypi/beetzbox/
