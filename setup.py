#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, invalid-name, wrong-import-position
"""
    SqueezeBox integration for Beets - A Beets plugin to integrate it with the SqueezeBox eco-system.

    This setuptools script follows the DRY principle and tries to
    minimize repetition of project metadata by loading it from other
    places (like the script module's ``__*__`` attributes). Incidently,
    this makes the script almost identical between different projects.

    It is also importable (by using the usual ``if __name__ == '__main__'``
    idiom), and exposes the project's setup data in a ``project`` dict.
    This allows other tools to exploit the data assembling code contained
    in here, and again supports the DRY principle. The ``rituals`` package
    uses that to provide Invoke tasks that work for any project, based on
    its project metadata.

    Copyright ©  2018 Jürgen Hermann <jh@web.de>

    Licensed under the MIT License, see "LICENSE" for details.
"""

project = dict(
    name='beetzbox',
    url='https://github.com/jhermann/beetzbox',
    license="MIT",
    keywords='squeezebox, music, beets, beets.plugin, media.management',

    packages=['beetsplug'],
    namespace_packages=['beetsplug'],
    install_requires=['beets>=1.4.3'],
    platforms=['ALL'],

    # Added by the code below:
    #   version author author_email (from script module)
    #   description (from doc string above)
    #   long_description (from README)
    #   classifiers (see below)
)

classifiers = """
# Details at http://pypi.python.org/pypi?:action=list_classifiers
Development Status :: 3 - Alpha
#Development Status :: 4 - Beta
#Development Status :: 5 - Production/Stable
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Environment :: Console
Intended Audience :: End Users/Desktop
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Topic :: Multimedia :: Sound/Audio
Topic :: Utilities
"""


# Beyond this point, code is not project-specific
import io
import os
import re
import sys
import json

try:
    from setuptools import setup
except ImportError as exc:
    raise RuntimeError("Cannot install '{0}', setuptools is missing ({1})"
                       .format(project['name'], exc))

project_root = os.path.abspath(os.path.dirname(__file__))
script_name = 'beetsplug/__init__.py'
expected_keys = "version author author_email".split()
with io.open(script_name, encoding='utf-8') as handle:
    for line in handle:
        match = re.match(r"""^__({})__ += (?P<q>['"])(.+?)(?P=q)$"""
                         .format('|'.join(expected_keys)), line)
        if match:
            project[match.group(1)] = match.group(3)

project.update(dict(
    description=__doc__.split('.')[0].split(' - ', 1)[1].strip(),
    long_description=(io.open('README.rst', encoding='UTF-8').read()
                      .split('\n.. _setup-start:', 1)[-1].strip()),
    classifiers=[i.strip()
                 for i in classifiers.splitlines()
                 if i.strip() and not i.strip().startswith('#')],
    keywords=project['keywords'].replace(',', ' ').strip().split(),
))

# Ensure 'setup.py' is importable by other tools, to access the project's metadata
__all__ = ['project', 'project_root']
if __name__ == '__main__':
    if '--metadata' in sys.argv[:2]:
        json.dump(project, sys.stdout, default=repr, indent=4, sort_keys=True)
        sys.stdout.write('\n')
    else:
        setup(**project)
