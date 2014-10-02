'''
Demonstrates utility scripting
'''

import os
from tempfile import TemporaryFile
from zipfile import ZipFile

import requests
import pandas as pd


def stata_to_csv(url, statafile, remove_stata=True):
    '''
    Download the 2006 US import data from the UC Davis Center for
    Economic Data, unzip, and convert to CSV format.

    `statafile` is the name of the .dta file within the ZIP file
    '''

    print('Downloading')
    response = requests.get(url)

    print('Writing to disk')
    temp = TemporaryFile()
    temp.write(response.content)

    print('Extracting')
    with ZipFile(temp) as tempzip:
        tempzip.extract(statafile)

    print('Loading into Pandas')
    df = pd.read_stata(statafile)

    csvfile = statafile.replace('.dta', '.csv')

    print('Writing CSV')
    df.to_csv(csvfile, index=False)

    if remove_stata:
        os.remove(statafile)


if __name__ == '__main__':

    url = 'http://cid.econ.ucdavis.edu/data/sasstata/usiss/imp06.zip'
    statafile = 'imp06_con.dta'

    stata_to_csv(url, statafile)
