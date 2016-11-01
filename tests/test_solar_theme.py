#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_solar_theme
----------------------------------

Tests for `solar_theme` module.
"""

import unittest


class TestSolar(unittest.TestCase):

    def setUp(self):
        pass

    def test_import_solar_theme(self):
        try:
            import solar_theme
        except ImportError:
            self.fail("!!! ERROR !!! -- Could not import 'solar_theme'")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
