#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
##
## Grundfos GENIBus Library for Arduino.
##
## (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
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

import wx

ID_CMD_REMOTE_LOCAL         = wx.NewIdRef()

ID_CMD_START_STOP           = wx.NewIdRef()

ID_CMD_MIN                  = wx.NewIdRef()
ID_CMD_MAX                  = wx.NewIdRef()

ID_CMD_RUN                  = wx.NewIdRef()
ID_CMD_PROGRAM              = wx.NewIdRef()
ID_CMD_CONST_FREQ           = wx.NewIdRef()
ID_CMD_CONST_PRESS          = wx.NewIdRef()
ID_CMD_PROP_PRESS           = wx.NewIdRef()
ID_CMD_REF_UP               = wx.NewIdRef()
ID_CMD_REF_DOWN             = wx.NewIdRef()
ID_CMD_AUTOADAPT            = wx.NewIdRef()
ID_CMD_NIGHT_REDUCE_E       = wx.NewIdRef()
ID_CMD_NIGHT_REDUCE_D       = wx.NewIdRef()
ID_CMD_LOCK_KEYS            = wx.NewIdRef()
ID_CMD_UNLOAD_KEYS          = wx.NewIdRef()
ID_CMD_RESET_ALARM          = wx.NewIdRef()
ID_CMD_RESET_ALARM_LOG      = wx.NewIdRef()

ID_MEAS_SPEED               = wx.NewIdRef()
ID_MEAS_HEAD                = wx.NewIdRef()
ID_MEAS_POWER               = wx.NewIdRef()
ID_MEAS_TEMPERATURE         = wx.NewIdRef()
ID_MEAS_DIFFPRESSURE        = wx.NewIdRef()
ID_MEAS_FLOW                = wx.NewIdRef()
ID_MEAS_ENERGY              = wx.NewIdRef()
ID_MEAS_HOURS               = wx.NewIdRef()
ID_MEAS_PERFORMANCE         = wx.NewIdRef()

ID_MEAS_SPEED_UNIT          = wx.NewIdRef()
ID_MEAS_HEAD_UNIT           = wx.NewIdRef()
ID_MEAS_POWER_UNIT          = wx.NewIdRef()
ID_MEAS_TEMPERATURE_UNIT    = wx.NewIdRef()
ID_MEAS_DIFFPRESSURE_UNIT   = wx.NewIdRef()
ID_MEAS_FLOW_UNIT           = wx.NewIdRef()
ID_MEAS_ENERGY_UNIT         = wx.NewIdRef()
ID_MEAS_HOURS_UNIT          = wx.NewIdRef()
ID_MEAS_PERFORMANCE_UNIT    = wx.NewIdRef()

ID_OPERATION_MODE           = wx.NewIdRef()
ID_SYSTEM_MODE              = wx.NewIdRef()
ID_CONTROL_SOURCE           = wx.NewIdRef()
ID_EXT_ANALOGUE             = wx.NewIdRef()
ID_TOTAL_INFLUENCE          = wx.NewIdRef()
ID_SETPOINT                 = wx.NewIdRef()
ID_ACTUAL_SETPOINT          = wx.NewIdRef()

ID_ALARM_ACTUAL             = wx.NewIdRef()
ID_ALARM_LOG1               = wx.NewIdRef()
ID_ALARM_LOG2               = wx.NewIdRef()
ID_ALARM_LOG3               = wx.NewIdRef()
ID_ALARM_LOG4               = wx.NewIdRef()
ID_ALARM_LOG5               = wx.NewIdRef()

ID_REF_REM                  = wx.NewIdRef()
ID_REF_IR                   = wx.NewIdRef()
ID_REF_ACT                  = wx.NewIdRef()
ID_SYS_FB                   = wx.NewIdRef()
ID_R_MIN                    = wx.NewIdRef()
ID_R_MAX                    = wx.NewIdRef()
ID_REF_REM_UNIT             = wx.NewIdRef()
ID_REF_IR_UNIT              = wx.NewIdRef()
ID_REF_ACT_UNIT             = wx.NewIdRef()
ID_SYS_FB_UNIT              = wx.NewIdRef()
ID_R_MIN_UNIT               = wx.NewIdRef()
ID_R_MAX_UNIT               = wx.NewIdRef()

ID_PARAM_UNIT_ADDR          = wx.NewIdRef()
ID_PARAM_GROUP_ADDR         = wx.NewIdRef()
ID_PARAM_H_CONST_REF_MIN    = wx.NewIdRef()
ID_PARAM_H_CONST_REF_MAX    = wx.NewIdRef()
ID_PARAM_H_PROP_REF_MIN     = wx.NewIdRef()
ID_PARAM_H_PROP_REF_MAX     = wx.NewIdRef()
ID_PARAM_UNIT_ADDR_UNIT       = wx.NewIdRef()
ID_PARAM_GROUP_ADDR_UNIT      = wx.NewIdRef()
ID_PARAM_H_CONST_REF_MIN_UNIT = wx.NewIdRef()
ID_PARAM_H_CONST_REF_MAX_UNIT = wx.NewIdRef()
ID_PARAM_H_PROP_REF_MIN_UNIT  = wx.NewIdRef()
ID_PARAM_H_PROP_REF_MAX_UNIT  = wx.NewIdRef()

ID_STR_PRODUCT_NAME         = wx.NewIdRef()
ID_STR_SOFTWARE_NAME1       = wx.NewIdRef()
ID_STR_COMPILE_DATE1        = wx.NewIdRef()
ID_STR_PROTOCOL_CODE        = wx.NewIdRef()
ID_STR_DEVELOPERS           = wx.NewIdRef()
ID_STR_SERIAL_NO            = wx.NewIdRef()

##
##
ID_SET_REFERENCE_VALUES     = wx.NewIdRef()
ID_SET_PARAMETER_VALUES     = wx.NewIdRef()
