import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# create datafram for spotifydata.xlsx

df = pd.read_excel(r"C:\\Users\\absim\\OneDrive\\Documents\\SpotifyData.xlsx", usecols="A")

# dataframe to str() to enable splitting

spotifyData = str(df)

returnList = spotifyData.split() # split the list
Counter = Counter(returnList)
topFive = Counter.most_common(5)

# store values from artist column into list
# most common function (5)
# num songs attributed to top (5) artists in top 50 

# plt.bar(topFive)
