#!/usr/bin/env python
"""CRC-Hilfsfunktionen fuer GENIBus-Telegramme."""

__version__ = "0.1.0"

__copyright__ = """
Grundfos GENIBus Library.

(C) 2007-2026 by Christoph Schueler <github.com/Christoph2,
                                     cpu12.gems@googlemail.com>

 All Rights Reserved

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""


import binascii
from collections.abc import Iterable


class CrcError(Exception):
    """Fehler bei CRC-Pruefung eines Telegramms."""

    pass


def calculate_crc(data: Iterable[int]) -> int:
    """Berechnet die GENIBus-CRC ueber die gegebenen Bytes.

    Args:
        data: Eingabebytes.

    Returns:
        int: 16-Bit-CRC-Wert.
    """
    return binascii.crc_hqx(bytearray(data), 0xffff) ^ 0xffff

def append_telegram(telegram: Iterable[int]) -> bytearray:
    """Haengt CRC-High/Low an ein Telegramm an.

    Args:
        telegram: Telegramm ohne CRC.

    Returns:
        bytearray: Telegramm inklusive angehaengter CRC-Bytes.
    """
    telegram = bytearray(telegram)
    crc = calculate_crc(telegram[1:])
    return telegram + bytearray([crc >> 8, crc & 0xff])

def check_telegram(telegram: Iterable[int], silent: bool = False) -> bool:
    """Prueft die CRC eines vollstaendigen Telegramms.

    Args:
        telegram: Telegramm inklusive CRC.
        silent: Wenn `True`, wird bei Fehlern kein `CrcError` geworfen.

    Returns:
        bool: `True` bei gueltiger CRC, sonst `False`.

    Raises:
        CrcError: Wenn CRC ungueltig ist und `silent=False`.
    """
    telegram = bytearray(telegram)
    match = calculate_crc(telegram[1:-2]) == (telegram[-2] << 8) + telegram[-1]
    if not match and not silent:
        raise CrcError('Telegram CRC not match!')
    else:
        return match
