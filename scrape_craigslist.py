'''
Scrape Davis housing data from Craigslist
'''

import requests
import bs4
import csv

davis_housing_url = ('http://sacramento.craigslist.org/search/'
        'apa?query=davis&sale_date=-')

craig_response = requests.get(davis_housing_url)

soup = bs4.BeautifulSoup(craig_response.content) 


def extract(tag):
    '''
    Extract relevant info from a single HTML tag
    '''
    try:
        price = tag.find('span', {'class':'price'}).text.replace('$', '')
        loc = tag.small.text
        desc = tag.find('span', {'class':'pl'}).a.text
        return price, loc, desc
    except AttributeError:
        return ('', '', '')


ptags = soup.find_all('p')

def to_csv(filename='price.csv'):
    '''
    Write extracted results to a CSV file
    '''
    with open(filename, 'w') as price:
        writer = csv.writer(price)
        writer.writerow(('price', 'location', 'description'))
        for tag in ptags:
            writer.writerow(extract(tag))

# Above a map could be used rather than the for loop
# writer.writerows(map(extract, ptags))

if __name__ == '__main__':
    to_csv()
