'''
Generate points on a polynomial

Replace this script with something more meaningful
'''

import math
import csv


def f(x):
    return x ** 2 + 5 * x + math.pi


data = [(x, f(x)) for x in range(-10, 10)]

with open('data.csv', 'w') as f:
    pen = csv.writer(f)
    pen.writerow(('x', 'y'))
    pen.writerows(data)
