'''
Scrape Davis housing data from Craigslist

Try running this script and then examining each of the
four intermediate data structures.
'''

import requests
import bs4
import csv

davis_housing_url = ('http://sacramento.craigslist.org/search/'
                     'apa?query=davis&sale_date=-')

# Make the network call
craig_response = requests.get(davis_housing_url)

# Parse the response using BeautifulSoup
craig_soup = bs4.BeautifulSoup(craig_response.content)

# Look in the 'p' tag elements to find just the actual listings
ptags = craig_soup.find_all('p')


def extract(tag):
    '''
    Extract relevant info from a single HTML tag.
    try / except block performs error handling for missing data
    '''
    try:
        price = tag.find('span', {'class': 'price'}).text.replace('$', '')
        loc = tag.small.text
        desc = tag.find('span', {'class': 'pl'}).a.text
        return price, loc, desc
    except AttributeError:
        return ('', '', '')


# Apply the extract function to every element in ptags
housing = map(extract, ptags)


def to_csv(content=housing, filename='davis_housing.csv'):
    '''
    Write extracted results to a CSV file
    '''
    with open(filename, 'w') as target:
        writer = csv.writer(target)

        # Add a row for the header
        writer.writerow(('price', 'location', 'description'))

        # Write in the main data
        writer.writerows(content)


# Statements inside this block will not run if the module is imported
if __name__ == '__main__':
    to_csv()
