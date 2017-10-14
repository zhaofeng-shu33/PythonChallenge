#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 expandtab:


"""
Welcome to the Python Challenge Project!

This project, based on PyUnit, is designed to assure that you have enough
knowledge and experiences in using Python, including basic variable operating,
data structure understanding, logic flow using, and complex tasking dealing.

Each challenge is consist of several functions. We will provide a set of inputs,
and your task is to fill the missing parts of the functions to return outputs as
required. The project will test your results, and when you have passed all tests,
you will succeed in this challenge.

Hope you enjoy the journey to the Wonderland of Python!

Yours sincerely,

ZhixingTHU.

================================================================================

- Instructions -

The project is based on PyUnit of Python 3.6, so you will have to install a
Python 3 version on your own PC. All tests are registered in `main.py`, and you
can run the tests either by running `main.py`, or using IDE (such as PyCharm)
PyUnit plug-ins.

================================================================================

- Example -

We give an example here.

def add(a, b):
    # ------ Your Code Here ------

    # ------ Your Code Ends ------
    return result

The `add` function is written to complete summation of two numbers. We guarantee
that the parameters `a` and `b` here are both integers, and you should return
the sum of these two numbers.

Integers can be positive or negative, or zero, but they all obey the `+` order
and behave well. We analyze the code, and see that the function receives
parameters `a` and `b`, then returns a variable `result`. In this case, we
should let `result` be the sum of `a` and `b`, so we fill `result = a + b` in
the missing part.

def add(a, b):
    # ------ Your Code Here ------
    result = a + b
    # ------ Your Code Ends ------
    return result

This will work, and for all possible parameters `a` and `b` (both integers), the
function returns the correct result.

Have a try yourself!

"""


def add(a, b):
    """
    This function completes summation of two integers.

    :param a: integer
    :param b: integer
    :return: sum of `a` and `b`

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


"""
If you have correctly filled the missing part above, and run PyUnit test now, 
you will find that nine marks in the first output line has turned `.` from `F`. 
This means you have passed the first nine tests of the project. Why nine? 
Because we wrote nine tests for this function alone.  

You can find the tests in `test.py` in the same folder. The Class `TestAdd` is
written to test this `add` function, and the nine functions in the class are the 
nine tests you have just passed.

All functions you are to complete are tested by testing classes and functions
like this. Maybe there will not be nine tests for each function, but we will try
our best to assure that your function is working properly. 

================================================================================

From this example, you can understand how the project works. As you can see, it
is really so young so simple, and maybe sometimes naive. But it works, though. 

So now it is your turn. Keep calm and code on! Beat up the following challenges!

See you later. 

"""


def mod_ten(number):
    """
    Every ten book is packed together. How many left?
    Calculate the remainder of any given non-negative number divided by ten.

    :param number: non-negative integer
    :return: remainder of `number` divided by ten

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def sphere_volume(radius):
    """
    Your cousin wants to know the volume of a sphere given a radius (cm).
    Calculate the answer, and make it accurate to two decimal places, rounding.

    :param radius: positive real number, 3.5 (cm)
    :return: 179.59 (cm^3)

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def say_hello(name):
    """
    You saw a friend on yor way home. Say hello to him, calling his name. That
    means, you should return a string in the following format.

    :param name: valid string, 'Alice'
    :return: 'Hello, Alice. How are you?'

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def list_count(item_list):
    """
    The function counts how many items are in the item list. You should add a
    number to the end of the list, and return the list. The number should be
    the item count of the list after you added the number.

    :param item_list: valid list, [1, 'Bob', None, {'5': 9}]  # 4 items
    :return: [1, 'Bob', None, {'5': 9}, 5]                    # added `5`

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def collatz_conjecture_index(number, index):
    """
    The famous Collatz Conjecture points out that, with any given positive
    integer, we do the following operations continuously:

    - if the number is odd, three times the number then add one
    - if the number is even, divide the number by two

    And at last, the sequence will always reach one.
    We give you a number, whose index is one, and we would like to know what the
    number would become at any given index.

    :param number: positive integer, 5
    :param index: positive integer, 3
    :return: 8

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def collatz_conjecture_end(number):
    """
    Still the Collatz Conjecture, but this time we would like to know, for a
    given positive integer, what index it would be when the sequence finally
    reaches one.

    :param number: positive integer, 5
    :return: 6

    """
    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def dictionary_lookup(dictionary, word):
    """
    The English Dictionary has so many words, their explanations and usages.
    Tom is hurrying for a class, so he left you the job: find the meaning of any
    given word. If the word is not in the dictionary, return 'Not Found!'.

    :param dictionary one-level python-dict format, each (k, v) pair is consist
                      of a word ant its explanation. Example:
                      {
                          'banana': 'A yellow fruit, grown in Singapore.',
                          'tomato': 'A red vegetable, sour.',
                      }
    :param word: valid string, 'banana'
    :return: 'A yellow fruit, grown in Singapore.'

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def indescribable_function(param):
    """
    The project designer became insanity, and he wrote this indescribable
    function. There is one input, no helping, and even no output declaration.
    Still, you have to make the function match every given single test case.

    :return: ???

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def judge_scores(score_list):
    """
    As we all know, in a contest where scores are given by judges, when
    calculating the final score of any player, the highest score and the lowest
    score are not used. The summation function is written, and we need your help
    to find out what scores are to be used later in summing.

    Please return a score list without the highest and the lowest scores,
    ascending by score.

    :param score_list: valid python-list with more than two scores, each unique
                       Example: [95.8, 80.9, 96.2, 93.7, 100.0, 95.6]
    :return: [93.7, 95.6, 95.8, 96.2]

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def gcd(a, b):
    """
    The Greatest Common Divisor is very useful in many math-related problems.
    Please find out the GCD of given positive integers `a` and `b`.

    :param a: positive integer, 12
    :param b: positive integer, 18
    :return: 6

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


class Book:
    """
    Each Book has an author and a publish year. We would like to check whether a
    book is written by a specific author. Please complete the `Book` class so
    that the following function `check_book_author` works properly.

    """

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    # ------ Your Code Here ------



    # ------ Your Code Ends ------

    def is_written_later(self, year):
        return self.year >= year


def check_book_author(book, author):
    """
    The function checks whether a book is written by a specific author.

    :param book: a `Book` class object, Book('Name', 'Author', 2017)
    :param author: valid string, 'Author'
    :return: boolean value `True`

    """

    return book.is_written_by(author)


"""
Congratulations! You have finished the basic challenge!

Now that you are digging deep into the hole, and try some real tasks! You can 
find them in t02_real_task package. 

"""
