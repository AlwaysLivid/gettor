# -*- coding: utf-8 -*-
#
# This file is part of GetTor, a Tor Browser distribution system.
#
# :authors: Panagiotis Vasilopoulos <hello@alwayslivid.com>
#           see also AUTHORS file
#
# :copyright:   (c) 2008-2014, The Tor Project, Inc.
#               (c) 2020, Panagiotis Vasilopoulos
#
# :license: This is Free Software. See LICENSE for license information.

import telebot
from telebot import types


class Telegram(object):
    """
    Class for sending twitter commands via the API.
    """

    def __init__(self, settings):
        """
        Constructor.

        """
        self.settings = settings

        telegram_key = self.settings.get("telegram_key")

        self.telegram_bot = telegram_oauth(telegram_key)

    def telegram_oauth(self, telegram_key):
        return telebot.AsyncTeleBot(token=telegram_key)
