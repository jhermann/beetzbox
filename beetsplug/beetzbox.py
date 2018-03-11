# -*- coding: utf-8 -*-
# pylint: disable=
""" Beetzbox – SqueezeBox integration.
"""
# Copyright ©  2018 Jürgen Hermann <jh@web.de>
#
# Licensed under the MIT License, see "LICENSE" for details.

from beets import ui
from beets.plugins import BeetsPlugin


class SqueezeBox(BeetsPlugin):
    """SqueezeBox plugin implementation."""

    def __init__(self):
        super().__init__()

    def commands(self):
        result = []

        command = ui.Subcommand('sq-play', help='add query results to playlist')
        command.func = self._play
        command.parser.add_album_option()
        command.parser.add_option('-i', '--insert', action='store_true', default=False,
            help='insert after current song, instead of adding at the end')
        result.append(command)

        return result

    def _play(self, lib, opts, args):
        """Execute a query and add the results to the current playlist."""
        print('sq-play:', lib, opts, args)
