#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import api

class TestApiMethods(unittest.TestCase):

    def test_get_members(self):
        self.assertEqual(type(api.get_members()), type([]))
    

if __name__ == '__main__':
    unittest.main()
