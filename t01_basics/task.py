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

    result = a + b

    # ------ Your Code Ends ------
    return result


"""
If you have correctly filled the missing part above, and run PyUnit test now, 
you will find that the first nine marks in the first output line turns `.` from 
`F`. This means you have passed the first nine tests of the project. Why nine? 
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

    result = number % 10

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

    PI = 3.1415926
    volume = 4 * PI * (radius ** 3) / 3
    result = float('%.2f' % volume)

    # ------ Your Code Ends ------
    return result


def say_hello(name):
    """
    You saw a friend on yor way home. Say hello to him, calling his name.
    That means, you should return the following string.

    :param name: valid string, 'Alice'
    :return: 'Hello, Alice. How are you?'

    """

    # ------ Your Code Here ------

    result = 'Hello, %s. How are you?' % name

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

    result = item_list
    result.append(len(item_list) + 1)

    # ------ Your Code Ends ------
    return result


"""
条件判断 if (odd *3+1 even /2)  for
循环 while
莫名其妙的函数（看 test 来写）
dict set
递归函数
list [-4:]
class
try-catch
"""


def gauss_problem():
    """


    :return:

    """

    return


def gcd(a, b):
    """

    :param a:
    :param b:
    :return:
    """

    return









"""
Congratulations! You have finished the basic challenge.

Now that you are digging deep into the hole, and try some real tasks!

"""
