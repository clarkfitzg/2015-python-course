'''
Script to download some interesting data from Github.com 

Thu Dec 18 17:13:16 PST 2014

There are about 25k repositories that match the query 'data science'.
We'll look at the most popular ones.
'''

import json
from requests import get


base = 'https://api.github.com/search/repositories'
payload = {'q': 'data science', 'sort': 'stars'}

response = get(base, params=payload)

# Creating intermediate variable for inspection
content = response.json()['items']

with open('datasci.json', 'w') as f:
    json.dump(content, f)
