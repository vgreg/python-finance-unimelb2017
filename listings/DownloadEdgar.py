#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 06:17:43 2017

@author: vincent

Prepared by [Vincent Grégoire](http://www.vincentgregoire.com), 
Department of Finance, The University of Melbourne. 

This is a sample code to illustrate how to automatically download all the
10-K filings from Edgar over a date range using Python. This is a very basic
illustration of how you can use Python for web scraping.
This notebook was created as supplemental material to a Python for 
financial research bootcamp for finance honours and PhD students at 
the University of Melbourne in March of 2017.

See https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm
for more details on accessing the SEC Edgar data.

Last update: March 27, 2017.

**Contact**: <vincent.gregoire@unimelb.edu.au>

Latest version: <http://www.vincentgregoire.com/python-bootcamp/>
"""

from os import listdir
import pandas as pd
import requests
 
# Two output directories, one for the 10-Ks, one for the Edgar index. They
# need to exist.
save_dir = '10K/'
index_dir = 'index/'

# First, download the index files.
start_year = 2000 # Min 1993
start_quarter = 1 # (1-4)
end_year = 2017
end_quarter = 1

# Generate the list of quarterly index files to download.
qtr_list1 = [(start_year, q+1) for q in range(start_quarter-1, 4)]
qtr_list2 = [(y, q+1) for y in range(start_year + 1, end_year)
             for q in range(4)]
qtr_list3 = [(end_year, q+1) for q in range(0, end_quarter)]
qtr_list = qtr_list1 + qtr_list2 + qtr_list3

# Download all the quarterly index files.
for y, q in qtr_list:
    url = ('https://www.sec.gov/Archives/edgar/full-index/' + str(y) 
           + '/QTR' + str(q) + '/master.gz')
    print('Downloading ' + str(y) + '-Q' + str(q) + ' ...')
    with open(index_dir + 'master_' + str(y) + '-Q' + str(q) + ' .gz', 'wb') as f:
        f.write(requests.get(url).content)
    print('Done')
    
# Load all index files in pandas.
idx_list = [x for x in listdir(index_dir) if not x.startswith('.')]
dfs = []
for x in idx_list:
    df = pd.read_csv(index_dir + x, delimiter='|',
                     names=['CIK', 'Company Name', 'Form Type',
                            'Date Filed', 'Filename'],
                     skiprows=11)
    dfs.append(df)
master = pd.concat(dfs)

# Extract only 10-Ks
master_10k = master[master['Form Type'] == '10-K']

# Get the Filename (includes part of the path.)
fn_list = [x for x in master_10k['Filename']]

# Download all the files
for fn in fn_list:
    url = 'https://www.sec.gov/Archives/' + fn
    print('Downloading ' + fn + ' ...')
    with open(save_dir + fn.split('/')[-1], 'wb') as f:
        f.write(requests.get(url).content)
    print('Done')