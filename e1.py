#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


url_va = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
req_va = requests.get(url_va)
html_va = req_va.content
soup = BeautifulSoup(html_va, 'html.parser')

tags = soup.find_all('tr', 'election_item')

ELECTION_ID = []
thefile = open('ELECTION_ID', 'w')
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    id = year + " " + year_id
    ELECTION_ID.append(id)

print(ELECTION_ID)

for item in ELECTION_ID:
  thefile.write("%s\n" % item)
