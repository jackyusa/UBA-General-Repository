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
df = pd.read_csv("inputRawFile.csv", index_col=False)

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
        (~df['ACCOUNT_NO.'].str.contains("1121",case=False))
    ].index,inplace=True)
    df.drop(df[
        (df['SCHEME_TYPE'] == 'OAP') &
        (~df['ACCOUNT_NO.'].str.contains("1121",case=False))
    ].index,inplace=True)

    df.to_csv('inputRawFile.csv',index=False)
    print("Irrelevant scheme types have been removed and account numbers containing 1121 have been saved - ✔")

###############################################################################################################################
# Set empty maturity dates to tomorrows date
# Set dates before today to tomorrow
def emptyMaturity():
    tomorrow_datetime = datetime.now() + timedelta(days=1)
    
    df['MATURITY_DATE'].fillna(tomorrow_datetime.date(), inplace=True)
    df['MATURITY_DATE'] = pd.to_datetime(df['MATURITY_DATE'],errors='coerce')
    df.to_csv('inputRawFile.csv',index=False)

    print("Empty Maturity_Date cells have been set to tomorrow's date: "+ str(tomorrow_datetime.date())+ " - ✔")

###############################################################################################################################
# Sorts the dataframe based on the Maturity date in ascending order
def sortByMaturity():
    tomorrow_datetime = datetime.now() + timedelta(days=1)

    x = len(df.index)
    for i in range(0,x):
        if type(df['MATURITY_DATE'][i]) == 'datetime.date':
            if((df['MATURITY_DATE'][i]) < datetime.now().date()):
                df['MATURITY_DATE'][i] = tomorrow_datetime.date()

    df.sort_values(by='MATURITY_DATE', ascending=True, inplace=True)
    df.to_csv('inputRawFile.csv',index=False)

    print("Maturity dates sorted sucessfully and old dates are set to tomorrow's date - ✔")

###############################################################################################################################
# Add a "AMOUNT" column after CLS_BALANCE column 
# then multiply CLS_BALANCE cells by -1
def addAmountColumn():
    df.insert(4,'AMOUNT','')
    x = len(df.index)
    non = "',"
    for i in range(0,x):
        # Fixes the formatting of CLS_BALANCE and sets it to a float type
        value = df['CLS_BALANCE'].values[i]
        for char in non: value=value.replace(char,"")
        value = float(value)
        df['AMOUNT'].values[i] = value * -1
    df.to_csv('inputRawFile.csv',index=False)
    print("Amount column has been inserted with negative values - ✔")

def insertColumn(columnName,index,values):
    df.insert(index,columnName,values)
    df.to_csv('inputRawFile.csv',index=False)
    print(columnName + " has been inserted into the dataframe in column " + index + "- ✔")

###############################################################################################################################
# Add USD column and covert AMOUNT to USD currency by the related conversion rate
# Add USD_AMOUNT after CURRENCY
def convertToUSD():
    df.insert(14,'USD_AMOUNT','')
    x = len(df.index)
    non = "',"
    for i in range(0,x):
        value = df['CLS_BALANCE'].values[i]
        for char in non: value=value.replace(char,"")
        value = float(value) * -1
        df['USD_AMOUNT'].values[i] = value * rates[df['CRNCY'].values[i]]
    df.to_csv('inputRawFile.csv',index=False)
    print("USD_AMOUNT column has been inserted and currencies have been converted to USD - ✔")

###############################################################################################################################
# Remove irrelevant columns
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
    df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
    df.to_csv('inputRawFile.csv')
    print("Irrelevant columns have been removed - ✔")

###############################################################################################################################
# Clears the file
def clearFile(file):
    f = open(file, "w")
    f.truncate()
    f.close()

###############################################################################################################################
# Go through the SCHEME_TYPES pull out CAA & ODA 
# make a file entry name dda  that is in columns
# "ACCOUNT_NO" & "ACCOUNT_NANE"  
# CALCULATE THE SUM FOR ALL USD_AMOUNT

def insertDDA():
    caa = df.loc[df['SCHEME_TYPE'] == 'CAA', 'USD_AMOUNT'].sum()
    oda = df.loc[df['SCHEME_TYPE'] == 'ODA', 'USD_AMOUNT'].sum()
    usd_sum = caa + oda

    dda1 = ['DDA', 'DDA', 'DDA','','','','',(datetime.now() + timedelta(days=1)),'',(usd_sum*0.1267)]
    dda2 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=6)),'',(usd_sum*0.2578)]
    dda3 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=8)),'',(usd_sum*0.0282)]
    dda4 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=15)),'',(usd_sum*0.0834)]
    dda5 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=30)),'',(usd_sum*0.0)]
    dda6 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=30)),'',(usd_sum*0.1387)]
    dda7 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=150)),'',(usd_sum*0.0596)]
    dda8 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=180)),'',(usd_sum*0.0)]
    dda9 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=365)),'',(usd_sum*0.0)]
    dda10 = ['DDA','DDA', 'DDA','','','','',(datetime.now() + timedelta(days=730)),'',(usd_sum*0.3056)]

    df.loc[df.shape[0]] = dda1
    df.loc[df.shape[0]] = dda2
    df.loc[df.shape[0]] = dda3
    df.loc[df.shape[0]] = dda4
    df.loc[df.shape[0]] = dda5
    df.loc[df.shape[0]] = dda6
    df.loc[df.shape[0]] = dda7
    df.loc[df.shape[0]] = dda8
    df.loc[df.shape[0]] = dda9
    df.loc[df.shape[0]] = dda10

    print("DDA row has been added to the bottom - ✔")
     # Fixing date formatting
    for i in range(0,len(df.index)):
        if(df['MATURITY_DATE'][i] != ''):
            date = df['MATURITY_DATE'][i]
            date.strftime('%Y-%m-%d')
            df['MATURITY_DATE'][i] = date.strftime('%Y-%m-%d')

    df.to_csv('inputRawFile.csv',index=False)

###############################################################################################################################
# Calls all functions
def fixFile():
    emptyMaturity()
    sortByMaturity()
    removeRows()
    addAmountColumn()
    convertToUSD()
    removeColumns()
    return(df)

insertDDA()