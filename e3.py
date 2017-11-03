
import glob
import pandas as pd

def clean_file(file):
    header = pd.read_csv(file, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(file, index_col = 0,
               thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = file.replace(".csv", "")
    df = df[["Democratic", "Republican", "Total Votes Cast", "Year"]]
    return df

all_files = glob.glob("*.csv")
dfs = []

for file in all_files:
    file = clean_file(file)
    dfs.append(file)

df = pd.concat(dfs)

df["Republican Share"] = df["Republican"] / df["Total Votes Cast"]
re_share = df[["Year", "Republican Share"]]

re_share.head()


county = "Accomack County"
mask = re_share.index == county

acc = re_share[mask]
acc.head()

def plot_county(df, county):
    mask = df.index == county
    cplot = df[mask]
    return cplot.plot(x = "Year")

test = plot_county(re_share, "Albemarle County")
