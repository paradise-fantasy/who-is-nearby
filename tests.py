#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import api
from Person import Person

class TestApiMethods(unittest.TestCase):

    def test_get_members(self):
        self.assertEqual(type(api.get_members()), type([]))

    def test_post_presence(self):
        person = Person(1, "Håvard","40:B8:37:2C:C6:9F", "blue", "paradise")
        print api.post_presence(person)
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
