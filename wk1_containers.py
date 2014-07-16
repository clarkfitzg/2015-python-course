'''
wk1_containers.py

Introduce basic data containers - list, tuple, set, dictionary, ndarray, DataFrame
'''

import numpy as np
import pandas as pd

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

# Composing these data structures is common.
# But mind the Zen of Python - 'Flat is Better than Nested'
pres_terms = {'obama': ('2015', '2009'), 
             'bush': ('2009', '2001'),
             'clinton': ('2001', '1993'),
             }

# TASK
# Compute how long each president was in office
from wk1_data_types import strdiff

# for loop, tuple unpacking
for key, value in pres_terms.items():
    print(key, strdiff(*value))
