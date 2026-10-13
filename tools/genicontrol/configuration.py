#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
##
## Grundfos GENIBus Library for Arduino.
##
## (C) 2007-2016 by Christoph Schueler <github.com/Christoph2,
##                                      cpu12.gems@googlemail.com>
##
##  All Rights Reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program; if not, write to the Free Software Foundation, Inc.,
## 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##
##

import configparser
import json

import logging
import os
import pkgutil
import threading

from genilib.utils import absConfigurationFilename
from genilib.utils.configprocessor import ConfigProcessor

CFG_FILE_NAME = absConfigurationFilename('.GeniControl.cfg')


def readConfigFile(project, fname):
    payload = pkgutil.get_data(project, 'config/%s' % fname)
    if payload is None:
        raise FileNotFoundError('Missing config file: %s' % fname)
    if isinstance(payload, bytes):
        payload = payload.decode('utf-8')
    return json.loads(payload)


class Config(object):
    _lock = threading.Lock()
    loaded = False

    def __new__(cls):
        # Double-Checked Locking
        if not hasattr(cls, '_instance'):
            try:
                cls._lock.acquire()
                if not hasattr(cls, '_instance'):
                    cls._instance = super(cls.__class__, cls).__new__(cls)
                    baz = readConfigFile("genicontrol", "GeniControl_Defaults.json")
                    cls.cp = ConfigProcessor(baz)
            finally:
                cls._lock.release()
        return cls._instance

    def __init__(self):
        pass

    def load(self):
        if not self.loaded:
            if os.access(CFG_FILE_NAME, os.F_OK):
                self.cp.read(open(CFG_FILE_NAME))
                self.loaded = True
        # else: we are working with default values.

    def save(self):
        self.cp.write(open(CFG_FILE_NAME, 'w'))

    def get(self, section, option):
        return self.cp.get(section, option)

    def set(self, section, option, value):
        self.cp.set(section, option, value)

