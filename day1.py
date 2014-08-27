'''
day1.py

Instructor Notes

These notes are meant to be a loose frame for the class period.
Instructors should type these from the Ipython interpreter.
Students should be encouraged to follow along.
Session should be highly interactive.

GENERAL THEME:
    The basics of Python

SPECIFIC TOPICS:
    - basic syntax
    - data types
    - containers
    - looping
'''

import numpy as np
import pandas as pd


############################################################
# basics
############################################################


# equals for variable assignment
x = 1

# Parentheses call functions
type(x)


############################################################
# data types - string, int, float, bool
############################################################


# What are possible basic data types?
ones = [1, 1.0, 'one', True]
zeros = [0, 0.0, 'zero', False]

# Compare comprehension to mathematical set syntax
types = [type(x) for x in ones]

# Try a few operators on different data types:
# +, -, ==, <,

# Error messages are meant to be informative.
True == 1

# These operators are calling magic methods
2.__add__

# TASK
# Compute the difference between these two years
pystarted = '1989'
now = '2015'

# TASK
# Could show evolution of this to a more general function
# start with return int(a) - int(b)
def strdiff(a, b):
    '''
    Converts a and b to numeric types returns the difference

    >>> strdiff('1989', '2000')
    11

    '''
    return abs(int(a) - int(b))


############################################################
# containers - ndarray, list, tuple, set, dictionary, DataFrame
############################################################


# ndarray
# Using namespace lookup - a honking good idea (Zen of Python)
normal = np.random.randn(10, 3)

# list
ones = [1, 1.0, 'one', True]

# tuple
ones = (1, 1.0, 'one', True)

# set
# switch to student names
names = {'obama', 'bush', 'clinton'}

# dict
# The most finely tuned data structure in the language
# The Python language is a big pile of connected dictionaries
presidents = {'obama': 2009, 'bush': 2001, 'clinton': 1993}

# hashable -- compare to md5 checksum on file when downloading Anaconda
# hashable <==> immutable <==> can be used as dict key

# TASK
# Determine which data types and containers are hashable
hash(ones)

# Composing these data structures is common.
# But mind the Zen of Python - 'Flat is Better than Nested'
pres_terms = {'obama': ('2015', '2009'),
              'bush': ('2009', '2001'),
              'clinton': ('2001', '1993'),
              }

# Observe- a trailing comma as in the above `pres_terms` will raise a syntax
# error in most languages, but not in Python. Why was this design chosen?


############################################################
# Looping
############################################################


# Iterable means you can loop over it
for i in range(10):
    print(i)

# TASK
# Compute how long each president was in office as of 2015

# for loop, tuple unpacking
for key, value in pres_terms.items():
    print(key, strdiff(*value))

# Note that dictionary keys don't seem to be sorted. Why?
