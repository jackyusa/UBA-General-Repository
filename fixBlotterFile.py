from operator import index
from re import T
from turtle import clear
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
from pkg_resources import empty_provider
from fixInputFile import *

clearFile('output.csv')
df = pd.read_csv("inputBlotterFile.csv", index_col=False)

x = len(df.index)
non = "',"
for i in range(0,x):
    if(type(df['Principal Amount (Signed)'].values[i]) == 'string'):
    # Fixes the formatting of CLS_BALANCE and sets it to a float type
        value = df['Principal Amount (Signed)'].values[i]
        for char in non: value=value.replace(char,"")
        value = float(value)
        df['Principal Amount (Signed)'].values[i] = value

df.rename(columns={"End Date": "MATURITY_DATE", "Principal Amount (Signed)":"USD_AMOUNT"},inplace=True)

keep = ['MATURITY_DATE','USD_AMOUNT']
df = df[keep]

df = pd.concat([firstFile(),df])
df.reset_index(drop=True,inplace=True)

tomorrow_datetime = (datetime.datetime.now().date() + timedelta(days=1))
df['MATURITY_DATE'].fillna(tomorrow_datetime, inplace=True)
df['MATURITY_DATE'] = pd.to_datetime(df['MATURITY_DATE'],errors='coerce')
df.sort_values(by='MATURITY_DATE', ascending=True, inplace=True)

df.loc[df['MATURITY_DATE'] < (pd.to_datetime("today")), "MATURITY_DATE"] = tomorrow_datetime

df.to_csv('output.csv',index=False)