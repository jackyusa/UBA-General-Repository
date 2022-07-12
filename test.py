from cmath import nan
import pandas as pd
from datetime import timedelta, datetime
import requests
from pkg_resources import empty_provider
import json

response = requests.get("https://v6.exchangerate-api.com/v6/81a98818ac24839899cdc992/latest/USD")
data = response.text
parse_json = json.loads(data)
rates = parse_json['conversion_rates']

df = pd.read_csv('inputTest.csv',index_col=0)

# test setting empty ones to 1 then changing them
def emptyDate():
    tomorrow_datetime = datetime.now() + timedelta(days=1)
    df['Date'].fillna(tomorrow_datetime.date(), inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df1 = df.sort_values(by="Date")
    df1.to_csv('inputTest.csv')

    print("All empty Maturity dates have been set to tomorrows date.")

def removeRows():
    df.drop(df[
        (df['Amount'] == 230) &
        (df.index.str.contains("a"))
    ].index,inplace=True)

    df.to_csv('inputTest.csv')

def clearFile():
    f = open('inputTest.csv', "w")
    f.truncate()
    f.close()

def addColumn():
    df.insert(2,'neg_Amount','')
    df.to_csv('inputTest.csv')

def convertToUSD():
    df.insert(4,'USD_Amount','')
    x = len(df.index)
    for i in range(0,x):
        df['USD_Amount'].values[i] = df['Amount'].values[i] * rates[df['Currency'].values[i]]
    df.to_csv('inputTest.csv')
convertToUSD()