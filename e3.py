#!/usr/bin/env python

import glob
import pandas as pd
import re

def clean_file(file):
    ## From Prof. Saxon: create column headers out of the second row in df
    header = pd.read_csv(file, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    # Replace column headers and drop rows with missing data
    df = pd.read_csv(file, index_col = 0,
               thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    # Add year and select only relevant columns
    df["Year"] = re.sub("[^0-9]", "", file)
    df = df[["Democratic", "Republican", "Total Votes Cast", "Year"]]
    return df

## Create list of dataframes from list of files
all_files = glob.glob("*.csv")
dfs = []

for file in all_files:
    file = clean_file(file)
    dfs.append(file)

# Create one df with results from all years
df = pd.concat(dfs)

# Create Republican Share column
df["Republican Share"] = df["Republican"] / df["Total Votes Cast"]*100
repub_share = df[["Year", "Republican Share"]]

# Function that makes line plots for counties
def plot_county(df, county):
    mask = df.index == county
    cplot = df[mask]
    cplot = cplot.plot(x = "Year", legend=False)
    cplot.set_xlabel("Election Year")
    cplot.set_ylabel("% Republican Votes")
    cplot.set_title("% Republican Votes in Presidential Elections"+" ("+county+")")
    vals = cplot.get_yticks()
    cplot.set_ylim(ymin = 0, ymax = 100)
    return cplot

## Create and save line plots for counties
accomack_county = plot_county(repub_share, "Accomack County")
accomack_county.figure.savefig('accomack_county.pdf')

albemarle_county = plot_county(repub_share, "Albemarle County")
albemarle_county.figure.savefig('albemarle_county.pdf')

alexandria_city = plot_county(repub_share, "Alexandria City")
alexandria_city.figure.savefig('alexandria_city.pdf')

alleghany_county = plot_county(repub_share, "Alleghany County")
alleghany_county.figure.savefig('alleghany_county.pdf')
