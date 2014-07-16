'''
wk1_data_types.py

Introduce basic data types - string, int, float, bool
Use the Ipython interpreter to learn
'''

# What are possible basic data types?
ones = [1, 1.0, 'one', True]
zeros = [0, 0.0, 'zero', False]

# Compare comprehension to mathematical set syntax
types = [type(x) for x in ones]

# Try a few operators on different data types: +, -, ==
# Note True == 1

# TASK
# Compute the difference between these two years
pystarted = '1989'
now = '2015'


# Could show evolution of this to a more general function
# start with return int(a) - int(b)
def strdiff(a, b):
    '''
    Converts a and b to numeric types returns the difference

    >>> strdiff('1989', '2000')
    11.0

    '''
    return abs(float(a) - float(b))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
