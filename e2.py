#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

for line in open("ELECTION_ID"):
    # Store id and year as separate variables for each row in ELECTION_ID
    id = line[5:10]
    year = line[0:4]
    # Insert each id in download file URL
    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
    base = base.format(id)
    # Write files to csv with year included in filename
    filename = "president_"+"general_"+year+".csv"
    with open(filename, 'w') as output:
        output.write(requests.get(base).text)
