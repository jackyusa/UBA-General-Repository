import pandas as pd
import numpy as np

df = pd.read_csv('sam.csv', index_col=0)

def addChar():
    df.index = "'" + df.index + "'" + ","
    df.to_csv('sam.csv')

addChar()