#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 expandtab:


import unittest

from t01_basics.task import *


class TestAdd(unittest.TestCase):
    def test_add_01_pos_pos(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_02_pos_zero(self):
        self.assertEqual(add(4, 0), 4)

    def test_add_03_pos_neg(self):
        self.assertEqual(add(5, -7), -2)

    def test_add_04_zero_pos(self):
        self.assertEqual(add(0, 1), 1)

    def test_add_05_zero_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_06_zero_neg(self):
        self.assertEqual(add(0, -11), -11)

    def test_add_07_neg_pos(self):
        self.assertEqual(add(-4, 8), 4)

    def test_add_08_neg_zero(self):
        self.assertEqual(add(-9, 0), -9)

    def test_add_09_neg_neg(self):
        self.assertEqual(add(-4, -9), -13)


class TestModTen(unittest.TestCase):
    def test_mod_ten_01(self):
        self.assertEqual(mod_ten(3), 3)

    def test_mod_ten_02(self):
        self.assertEqual(mod_ten(125), 5)

    def test_mod_ten_03(self):
        self.assertEqual(mod_ten(30), 0)

    def tes_mod_ten_04(self):
        self.assertEqual(mod_ten(0), 0)


class TestSphereVolume(unittest.TestCase):
    def test_sphere_volume_01(self):
        self.assertEqual(sphere_volume(3.5), 179.59)

    def test_sphere_volume_02(self):
        self.assertEqual(sphere_volume(6.23), 1012.87)


class TestSayHello(unittest.TestCase):
    def test_say_hello_01(self):
        self.assertEqual(say_hello('Jenny'), 'Hello, Jenny. How are you?')

    def test_say_hello_02(self):
        self.assertEqual(say_hello('@#\'4'), 'Hello, @#\'4. How are you?')


class TestListCount(unittest.TestCase):
    def test_list_count_01(self):
        self.assertEqual(
            list_count([1, 'Bob', None, {'5': 9}]),
            [1, 'Bob', None, {'5': 9}, 5]
        )

    def test_list_count_02(self):
        self.assertEqual(list_count([]), [1])

