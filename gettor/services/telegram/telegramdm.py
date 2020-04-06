# -*- coding: utf-8 -*-
#
# This file is part of GetTor, a Tor Browser distribution system.
#
# :authors: Panagiotis Vasilopoulos <hello@alwayslivid.com>
#           see also AUTHORS file
#
# :copyright:   (c) 2008-2014, The Tor Project, Inc.
#               (c) 2019, Hiro
#
# :license: This is Free Software. See LICENSE for license information.

from __future__ import absolute_import

import time

# from ...parse.telegram import TelegramParser
from ...utils.telegram import Telegram
from ...utils.commons import log


class Telegramdm(object):
    def __init__(self, settings):
        """
        Constructor.

        """
        self.settings = settings
        self.telegram = Telegram(settings)

    def get_interval(self):
        """
        Get time interval for service periodicity.

        : return: time interval(float) in seconds.
        """
        return self.settings.get("telegram_interval")

    def telegram_callback(self, message):
        """
        Callback invoked after a message has been sent.

        : param message(string): Success details from the server.
        """
        log.info("Telegram: Message sent successfully.")

    def telegram_errback(self, error):
        """
        Errback if we don't/can't send the message.
        """
        log.debug("Telegram: Could not send message.")
        raise RuntimeError("{}".format(error))

    def telegramdm(self, error):
        """
        TO-DO: Add reply mechanism here, use it in get_new().
        """
        pass

    def get_new(self):
        """
        TO-DO: Add listener here?
        """
        pass