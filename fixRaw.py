from re import T
import pandas as pd
import numpy as np
from datetime import timedelta, datetime
import requests
from pkg_resources import empty_provider
import json

response = requests.get("https://v6.exchangerate-api.com/v6/81a98818ac24839899cdc992/latest/USD")
data = response.text
parse_json = json.loads(data)
rates = parse_json['conversion_rates']

###############################################################################################################################
# Creates the dataframe for the file
df = pd.read_csv("inputTest.csv", index_col=0)

###############################################################################################################################
# Remove rows that are not ODA/CAA/LAA or OAB/OAP that
# the account number doesn't have 1121 in the 7th place
def removeRows():
    # First filter out those that aren't ODA/CAA/LAA/OAP/OAB
    df.drop(df[
        (df['SCHEME_TYPE'] != "ODA") &
        (df['SCHEME_TYPE'] != "CAA") &
        (df['SCHEME_TYPE'] != "LAA") &
        (df['SCHEME_TYPE'] != "OAP") &
        (df['SCHEME_TYPE'] != "OAB")].index, inplace=True)
    
    # Find where rows are OAB/OAP and dont have 1121 in the
    # account number and remove them
    df.drop(df[
        (df['SCHEME_TYPE'] == 'OAB') &
        (~df.index.str.contains("1121",case=False))
    ].index,inplace=True)
    df.drop(df[
        (df['SCHEME_TYPE'] == 'OAP') &
        (~df.index.str.contains("1121",case=False))
    ].index,inplace=True)

    df.to_csv('inputRawFile.csv')
    print("Irrelevant scheme types have been removed and account numbers containing 1121 have been saved.")

###############################################################################################################################
# Set empty maturity dates to tomorrows date
def emptyMaturity():
    tomorrow_datetime = datetime.now() + timedelta(days=1)
    
    df['MATURITY_DATE'].fillna(tomorrow_datetime.date(), inplace=True)
    df['MATURITY_DATE'] = pd.to_datetime(df['MATURITY_DATE'],errors='coerce')
    df.to_csv('inputRawFile.csv')

    print("Empty Maturity_Date cells have been set to tomorrow's date: "+ tomorrow_datetime)

###############################################################################################################################
# Sorts the dataframe based on the Maturity date in ascending order
def sortByMaturity():
    df["MATURITY_DATE"] = pd.to_datetime(df["MATURITY_DATE"])
    df1 = df.sort_values(by='MATURITY_DATE')
    df.to_csv('inputRawFile.csv')

    print("Maturity dates sorted sucessfully!")

###############################################################################################################################
# Add a "AMOUNT" column after CLS_BALANCE column 
# then multiply CLS_BALANCE cells by -1
def addAmountColumn():
    df.insert(4,'AMOUNT','')
    df['AMOUNT'] = df['CLS_BALANCE'] * -1
    df.to_csv('inputRawFile.csv')
    print("Amount column has been inserted with negative values")

def insertColumn(columnName,index,values):
    df.insert(index,columnName,values)
    df.to_csv('inputRawFile.csv')
    print(columnName + " has been inserted into the dataframe in column " + index)

###############################################################################################################################
# add USD column and covert AMOUNT to USD currency by the related conversion rate
# add USD_AMOUNT after CURRENCY
def convertToUSD():
    df.insert(9,'USD_AMOUNT','')
    x = len(df.index)
    for i in range(0,x):
        df['USD_AMOUNT'].values[i] = df['CLS_BALANCE'].values[i] * rates[df['CRNCY'].values[i]]
    df.to_csv('inputRawFile.csv')
    print("USD_AMOUNT column has been inserted and currencies have been converted to USD")

###############################################################################################################################
def fixFile():
    emptyMaturity()
    sortByMaturity()
    removeRows()

###############################################################################################################################
# clears the file
def clearFile(file):
    f = open(file, "w")
    f.truncate()
    f.close()