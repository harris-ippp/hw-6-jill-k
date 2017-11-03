#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

for line in open("ELECTION_ID"):
    id = line[5:10]
    year = line[0:4]
    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
    base = base.format(id)
    filename = year+".csv"
    with open(filename, 'w') as output:
        output.write(requests.get(base).text)
