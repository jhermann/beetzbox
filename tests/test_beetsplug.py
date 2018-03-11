# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, missing-docstring, no-self-use, bad-continuation
""" Test «beetsplug».
"""
# Copyright ©  2018 Jürgen Hermann <jh@web.de>
#
# Licensed under the MIT License, see "LICENSE" for details.
from beetsplug import *
from beetsplug import __version__ as version


def test_version_is_numeric_semver():
    assert all(x.isdigit() for x in version.split('.')[:3])
