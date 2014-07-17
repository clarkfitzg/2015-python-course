'''
Generate random uniform numbers and save to file

Replace this script with something more meaningful
'''

import random
import csv


random.seed(37)

data = ((i, random.random()) for i in range(10))

with open('data.csv', 'w') as f:
    pen = csv.writer(f)
    pen.writerows(data)
