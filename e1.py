#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

# Parse contents of all VA election data
url_va = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
req_va = requests.get(url_va)
html_va = req_va.content
soup = BeautifulSoup(html_va, 'html.parser')

# Find all rows with election_item class
tags = soup.find_all(class_ = 'election_item')

# Extract all election years and ids and store in list
ELECTION_ID = []
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    id = year + " " + year_id
    ELECTION_ID.append(id)

# Write ids and years to file
thefile = open('ELECTION_ID', 'w')
for item in ELECTION_ID:
  thefile.write("%s\n" % item)
