```
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy.stats import norm
import pandas as pd
from csv import reader
import os
import re

def plot_density(dir, kmer):
    file_name = os.path.join(dir, kmer + "_mu.csv")
    df = pd.read_csv(file_name)
    import seaborn as sns
    # plotting histogram for carat using distplot()
    sns.distplot(a=df.mu, hist=True, bins=100)

    # visualizing plot using matplotlib.pyplot library
    plt.title(kmer)
    plt.show()
```
