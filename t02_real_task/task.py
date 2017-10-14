#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 expandtab:


"""
We introduce some real tasks here.

================================================================================

- Story Background -

A class has a set of students, each having a name, an age, a gender, and a cell
number, etc. The class manager often receives requirements from his boss, such
as listing all names, or counting how many boys or girls are in the class.

With only one class, the manager can do the work by hand, like a piece of cake.
However, one day, the manager is asked to response to the requests on all
classes in the world...and consider how much work that would be!

The manager decided to write some programs to free himself from this homogeneity
labor, and he asked you for help.

================================================================================

- Requirements -

This file contains a series of data packet operating functions, and you have to
complete the missing parts. Each function is given a data packet(dict format),
and your task is to return a dict meeting the conditions.

The given packet is under the format following...

{
    'className': STRING_OF_CLASS_NAME,
    'students': [{
        'name': STRING_OF_STUDENT_NAME,
        'age': INTEGER_OF_STUDENT_AGE,          # non-negative
        'gender': STRING_OF_STUDENT_GENDER,     # either 'male' or 'female'
        'cell': STRING_OF_STUDENT_CELL_NUMBER,  # len() = 11
    }, ...],
}

For example, the data packet can be:

{
    'className': 'Math',
    'students': [{
        'name': 'Peter',
        'age': 21,
        'gender': 'male',
        'cell': '15803062590',
    }, {
        'name': 'Mary',
        'age': 19,
        'gender': 'female',
        'cell': '13911756789',
    }],
}

This example packet will be used to show you what the output format should be.
All 'example packet's blow refer to this two-student-Math-class packet.

================================================================================

- Attention! -

The program should work for different classes, so your function may receive data
packet from any class, where all packets follow the format above. We will test
your work with different packets, and it should work with all of them.

"""


def get_names(packet):
    """
    The School Master wants a student name list from the given class. The order
    of students should be the same as given.

    :param packet: see the 'example packet'
    :return:

    {
        'names': ['Peter', 'Mary'],
    }

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result


def filter_age(packet, valid_age):
    """
    The TV Chanel is playing videos, but the videos are forbidden to students
    too young. Each video has its own valid age line, and only students who are
    older than this line can watch the video. Please find out who can watch the
    video for any given age line. The order of students should be descending by
    their age, then ascending by name lexicographic order.

    :param packet: see the 'example packet'
    :param valid_age: positive integer, 20
    :return:

    {
        'className': 'Math'
        'valid_count': 1,
        'students': [{
            'name': 'Peter',
            'age': 21,
            'gender': 'male',
            'cell': '15803062590',
        }],
    }

    """

    # ------ Your Code Here ------



    # ------ Your Code Ends ------
    return result
