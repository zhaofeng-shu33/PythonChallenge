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
        self.assertEqual(
            list_count([2, None, {'5': 9}, 'Je']),
            [2, None, {'5': 9}, 'Je', 5]
        )

    def test_list_count_03(self):
        self.assertEqual(list_count([]), [1])


class TestCollatzConjectureIndex(unittest.TestCase):
    def test_collatz_conjecture_index_01(self):
        self.assertEqual(collatz_conjecture_index(5, 3), 8)

    def test_collatz_conjecture_index_02(self):
        self.assertEqual(collatz_conjecture_index(18, 1), 18)

    def test_collatz_conjecture_index_03(self):
        self.assertEqual(collatz_conjecture_index(355, 1234), 4)


class TestCollatzConjectureEnd(unittest.TestCase):
    def test_collatz_conjecture_end_01(self):
        self.assertEqual(collatz_conjecture_end(5), 6)

    def test_collatz_conjecture_end_02(self):
        self.assertEqual(collatz_conjecture_end(355), 33)

    def test_collatz_conjecture_end_03(self):
        self.assertEqual(collatz_conjecture_end(1), 1)


class TestIndescribableFunction(unittest.TestCase):
    def test_indescribable_function_01(self):
        self.assertEqual(indescribable_function(1), 2)

    def test_indescribable_function_02(self):
        self.assertEqual(indescribable_function(2), 4)

    def test_indescribable_function_03(self):
        self.assertEqual(indescribable_function(4), 7)

    def test_indescribable_function_04(self):
        self.assertEqual(indescribable_function(7), 5)

    def test_indescribable_function_05(self):
        self.assertEqual(indescribable_function(9), 0)

    def test_indescribable_function_06(self):
        self.assertEqual(indescribable_function(0), None)

    def test_indescribable_function_07(self):
        self.assertEqual(indescribable_function('Harry'), 'Harry Potter')

    def test_indescribable_function_08(self):
        self.assertEqual(indescribable_function('Alice'), 'Bob')

    def test_indescribable_function_09(self):
        self.assertEqual(indescribable_function({
            'type': 'B',
            'part': ('USB', 'VGA', 'iPhone'),
        }), ['VGA', 'iPhone'])

    def test_indescribable_function_10(self):
        self.assertEqual(indescribable_function({
            'type': 'B',
            'part': ('USB-C', 'VGA', 'iPhone'),
        }), 'Apple')


class TestDictionaryLookup(unittest.TestCase):
    def setUp(self):
        self.dictionary = {
            'banana': 'A yellow fruit, grown in Singapore.',
            'missing': 'Not Found!',
            'tomato': 'A red vegetable, sour.',
        }

    def test_dictionary_lookup_01(self):
        self.assertEqual(
            dictionary_lookup(self.dictionary, 'banana'),
            'A yellow fruit, grown in Singapore.'
        )

    def test_dictionary_lookup_02(self):
        self.assertEqual(
            dictionary_lookup(self.dictionary, 'missing'),
            'Not Found!'
        )

    def test_dictionary_lookup_03(self):
        self.assertEqual(
            dictionary_lookup(self.dictionary, 'apple'),
            'Not Found!'
        )

    def tearDown(self):
        self.dictionary = None


class TestJudgeScores(unittest.TestCase):
    def test_judge_scores_01(self):
        self.assertEqual(
            judge_scores([95.8, 80.9, 96.2, 93.7, 100.0, 95.6]),
            [93.7, 95.6, 95.8, 96.2]
        )

    def test_judge_scores_02(self):
        self.assertEqual(judge_scores([7, 5, 6]), [6])


class TestGCD(unittest.TestCase):
    def test_gcd_01(self):
        self.assertEqual(gcd(12, 18), 6)

    def test_gcd_02(self):
        self.assertEqual(gcd(37, 59), 1)

    def test_gcd_03(self):
        self.assertEqual(gcd(20171014, 12345678), 2)


class TestCheckBookAuthor(unittest.TestCase):
    def setUp(self):
        self.book = Book('Harry Potter', 'J.K. Rowling', 1997)

    def test_check_book_author_01(self):
        self.assertEqual(check_book_author(self.book, 'J.K. Rowling'), True)

    def test_check_book_author_02(self):
        self.assertEqual(check_book_author(self.book, 'J.P. Rowling'), False)
