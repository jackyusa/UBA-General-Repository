from operator import index
from re import T
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
import requests
from pkg_resources import empty_provider
import json

response = requests.get("https://v6.exchangerate-api.com/v6/81a98818ac24839899cdc992/latest/USD")
data = response.text
parse_json = json.loads(data)
rates = parse_json['conversion_rates']

df = pd.read_csv('inputRawFile.csv', index_col=False)

def removeColumns():
    del df['AVG_CR_BALANCE']
    del df['AVG_DR_BALANCE']
    del df['INT_EXPENSE']
    del df['INT_INCOME']
    del df['GL_SUB_HEAD_CODE']
    del df['A/C_CLASSIFICATION']
    del df['CR_INT_RATE']
    del df['DR_INT_RATE']
    del df['COUNTRY']
    del df['INT_CODE']
    del df['LAST_DAY_IN_DR_BAL']
    del df['INT_PAY_FLAG']
    del df['INT_COLL_FLAG']
    del df['CUST_ID']
    del df['OPENING_BAL.']
    df.drop(df.columns[len(df.columns)-1],axis=1,inplace=True)
    df.to_csv('output.csv',index=False)

def clearFile(file):
    f = open(file, "w")
    f.truncate()
    f.close()

def emptyMaturity():
    tomorrow_datetime = datetime.datetime.now().date() + timedelta(days=1) # datetime.date type
    today_datetime = datetime.datetime.now().date()

    df['MATURITY_DATE'].fillna(tomorrow_datetime, inplace=True) # datetime.date type
    df['MATURITY_DATE'] = pd.to_datetime(df['MATURITY_DATE'],errors='coerce')
    df.dropna(inplace=True)

    for i in range(1,len(df.index)):
        df['MATURITY_DATE'][i] = pd.to_datetime(df['MATURITY_DATE'][i])
        print(type(df['MATURITY_DATE'][i]))

    df.sort_values(by='MATURITY_DATE', ascending=True, inplace=True)
    df.to_csv('output.csv',index=False)

def addAmountColumn():
    df['AMOUNT'] = pd.Series(dtype='int')
    df.to_csv('output.csv')

clearFile('output.csv')
removeColumns()
emptyMaturity()
addAmountColumn()