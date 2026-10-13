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

__all__ = [
    'COMMANDS', 'MEASUREMENT_VALUES', 'REFERENCES', 'PARAMETER', 'STRINGS', 'SIXTEENBIT_MEASUREMENT_VALUES',
    'DATAITEMS', 'defs.Access.RO', 'defs.Access.WO', 'defs.Access.WR'
]

from collections import namedtuple
import json
from pathlib import Path

import genibus.gbdefs as defs

_DEVICE_MODELS_DIR = Path(__file__).resolve().parents[2] / 'src' / 'genibus' / 'devices'

Dataitem = namedtuple('Dataitem', 'name klass id access note')

# Module-level lazy-loaded cache
_loaded = False
_current_model = None


def _load_model_data(model_name: str):
    """Load a model definition from the canonical JSON device files."""
    model_file = _DEVICE_MODELS_DIR / f'{model_name}.json'
    with model_file.open('r', encoding='utf-8') as handle:
        raw_data = json.load(handle)
    return [
        Dataitem(item[0], item[1], item[2], item[3], item[4])
        for item in raw_data
    ]


def load_model(model_name: str = 'magna'):
    """Reload the module data for a specific device model."""
    global _loaded, _current_model
    dataitems_data = _load_model_data(model_name)
    _current_model = model_name
    _loaded = False
    _initialize()
    return dataitems_data


def _initialize():
    """Initialize all data structures from the canonical JSON device model."""
    global _loaded, _current_model

    if _loaded and _current_model is not None:
        return

    raw_data = _load_model_data(_current_model or 'magna')

    # Convert raw dicts to Dataitem namedtuples
    dataitems_data = raw_data
    
    # Initialize dictionaries by class
    protocol_data = {}
    commands = {}
    measurement_values = {}
    references = {}
    parameter = {}
    strings = {}
    sixteenbit_measurement_values = {}

    def addToDict(d, k, v):
        d[k] = v

    for item in dataitems_data:
        if item.klass == 0:
            addToDict(protocol_data, item.name, item)
        elif item.klass == 2:
            addToDict(measurement_values, item.name, item)
        elif item.klass == 3:
            addToDict(commands, item.name, item)
        elif item.klass == 4:
            addToDict(parameter, item.name, item)
        elif item.klass == 5:
            addToDict(references, item.name, item)
        elif item.klass == 7:
            addToDict(strings, item.name, item)
        elif item.klass == 11:
            addToDict(sixteenbit_measurement_values, item.name, item)

    dataitems_for_class = {
        defs.APDUClass.PROTOCOL_DATA:               protocol_data,
        defs.APDUClass.MEASURED_DATA:               measurement_values,
        defs.APDUClass.COMMANDS:                    commands,
        defs.APDUClass.CONFIGURATION_PARAMETERS:    parameter,
        defs.APDUClass.REFERENCE_VALUES:            references,
        defs.APDUClass.ASCII_STRINGS:               strings,
        defs.APDUClass.SIXTEENBIT_MEASURED_DATA:    sixteenbit_measurement_values
    }

    def dataItemsById(klass):
        d = dataitems_for_class[klass]
        return {v.id: (v.name, v.access, v.note) for v in d.values()}
    
    def dataItemsByName(klass):
        d = dataitems_for_class[klass]
        return {k: (v.id, v.access, v.note) for k, v in d.items()}

    dataitems_by_id = {k: dataItemsById(k) for k in dataitems_for_class.keys()}
    dataitems_by_name = {k: dataItemsByName(k) for k in dataitems_for_class.keys()}
    
    # Update module globals
    globals()['DATAITEMS'] = dataitems_data
    globals()['PROTOCOL_DATA'] = protocol_data
    globals()['COMMANDS'] = commands
    globals()['MEASUREMENT_VALUES'] = measurement_values
    globals()['REFERENCES'] = references
    globals()['PARAMETER'] = parameter
    globals()['STRINGS'] = strings
    globals()['SIXTEENBIT_MEASUREMENT_VALUES'] = sixteenbit_measurement_values
    globals()['DATAITEMS_FOR_CLASS'] = dataitems_for_class
    globals()['DATAITEMS_BY_ID'] = dataitems_by_id
    globals()['DATAITEMS_BY_NAME'] = dataitems_by_name
    
    _loaded = True


def __getattr__(name):
    """Lazy load data on first access."""
    if name in ('DATAITEMS', 'PROTOCOL_DATA', 'COMMANDS', 'MEASUREMENT_VALUES', 'REFERENCES',
                'PARAMETER', 'STRINGS', 'SIXTEENBIT_MEASUREMENT_VALUES', 'DATAITEMS_FOR_CLASS',
                'DATAITEMS_BY_ID', 'DATAITEMS_BY_NAME'):
        _initialize()
        # Now that it's initialized, return the value from globals
        return globals()[name]
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# json.dump(DATAITEMS, open(r'C:\Users\christoph303\Documents\Arduino\libraries\Genibus\tools\genicontrol\config\dataitems.json', 'w'))

"""
Code Alarm Group Alarm Cause
2  Missing Phase
32 Overvoltage
40 Undervoltage
48 Overload
49 Overcurrent (i_mo)
51 Blocked motor/pump
56 Underload
57 Dry Running
58 Low Flow
64 Overtemperature
65 Motor Temperature (t_m)
66 Control Electronics Temperature (t_e)
67 Power Converter Temperature (t_m)
68 External Temperature / Water Temperature (t_w)
72 Hardware Fault type 1
73 Hardware Shut Down (HSD)
74 Internal Supply Voltage too high
75 Internal Supply Voltage too low
76 Internal Communication failure
77 Twin Pump Communication failure
152 Add On Module Communication Fault
80 Hardware Fault type 2
83 FE Parameter Area Verification error (EEPROM)
85 BE Parameter Area Verification error (EEPROM)
88 Sensor Fault
89 (Feedback) Sensor 1 signal fault
90 RPM Sensor signal fault
91 Temperature Sensor signal fault
92 (Feedback) Sensor calibration fault
"""
