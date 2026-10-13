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


from collections import namedtuple
import json

from genilib.configuration import readConfigFile

ValueTuple = namedtuple('ValueTuple', 'header unit range zero value')
Unit = namedtuple('Unit', 'physEntity factor unit')

_raw_units = readConfigFile("genicontrol", "units.json")

# Convert dicts to Unit namedtuples. JSON object keys are strings, so coerce them to int.
UnitTable = {}
for key, unit_data in _raw_units.items():
    unit_id = int(key)
    UnitTable[unit_id] = Unit(unit_data['physEntity'], unit_data['factor'], unit_data['unit'])


