#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 expandtab:


import unittest

from t02_real_task.task import *


class TestDataOperation(unittest.TestCase):
    def setUp(self):
        self.packet = {
            'className': 'Algorithms',
            'students': [{
                'name': 'Alice',
                'age': 18,
                'gender': 'female',
                'cell': '13395322680',
            }, {
                'name': 'Bob',
                'age': 22,
                'gender': 'male',
                'cell': '15019233039',
            }, {
                'name': 'Catherine',
                'age': 21,
                'gender': 'female',
                'cell': '13439821634',
            }, {
                'name': 'David',
                'age': 16,
                'gender': 'male',
                'cell': '18643639877',
            }, {
                'name': 'Emily',
                'age': 25,
                'gender': 'female',
                'cell': '15549307829',
            }, {
                'name': 'Edward',
                'age': 25,
                'gender': 'male',
                'cell': '15835892250',
            }],
        }

    def test_get_names(self):
        result = {
            'names': ['Alice', 'Bob', 'Catherine', 'David', 'Emily', 'Edward']
        }
        self.assertEqual(get_names(self.packet), result)

    def test_filter_age(self):
        result = {
            'className': 'Algorithms',
            'valid_count': 4,
            'students': [{
                'name': 'Edward',
                'age': 25,
                'gender': 'male',
                'cell': '15835892250',
            }, {
                'name': 'Emily',
                'age': 25,
                'gender': 'female',
                'cell': '15549307829',
            }, {
                'name': 'Bob',
                'age': 22,
                'gender': 'male',
                'cell': '15019233039',
            }, {
                'name': 'Catherine',
                'age': 21,
                'gender': 'female',
                'cell': '13439821634',
            }],
        }
        self.assertEqual(filter_age(self.packet, 20), result)
