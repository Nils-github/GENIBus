#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

__copyright__ = """
Grundfos GENIBus Library.

(C) 2007-2017 by Christoph Schueler <github.com/Christoph2,
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

import threading
import unittest

from genibus.devices.db import DataitemByClass, DeviceDB


class TestAPDUs(unittest.TestCase):

    def setUp(self):
        self.db = DeviceDB()

    def tearDown(self):
        del self.db

    def testUnitsByEntity(self):
        self.assertEqual(self.db.unitsByEntity("Voltage"), [(3, 'Voltage', 0.1, 'V'),
             (4, 'Voltage', 1.0, 'V'),
             (5, 'Voltage', 5.0, 'V'),
             (104, 'Voltage', 2.0, 'V')])

    def testDataItemByClassName(self):
        self.assertEqual(
            self.db.dataitemByClassAndName("magna", "ref_loc"),
            DataitemByClass(40, 2, 1, 'Local reference setting'),
        )

    def testDatabaseCanBeUsedFromAnotherThread(self):
        results = []
        errors = []

        def query_units():
            try:
                for _ in range(25):
                    results.append(self.db.unitsByEntity("Voltage"))
            except Exception as error:
                errors.append(error)

        workers = [threading.Thread(target=query_units) for _ in range(4)]
        for worker in workers:
            worker.start()
        for worker in workers:
            worker.join()

        self.assertEqual(errors, [])
        self.assertEqual(len(results), 100)
        self.assertTrue(all(result == results[0] for result in results))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
