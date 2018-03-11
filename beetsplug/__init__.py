# -*- coding: utf-8 -*-
# pylint: disable=
""" Beetzbox plugin namespace package.
"""
# Copyright ©  2018 Jürgen Hermann <jh@web.de>
#
# Licensed under the MIT License, see "LICENSE" for details.
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
__import__('pkg_resources').declare_namespace(__name__)

__version__ = '0.1.0'
__author__ = 'Jürgen Hermann'
__author_email__ = 'jh@web.de'
