import pandas as pd
import numpy as np
from datetime import timedelta, datetime

df = pd.read_csv('rawFile.csv',index_col=0)

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
    df['ACCOUNT_NO.'] = df['ACCOUNT_NO.'].apply(str)
    df.drop(df[
        (df['SCHEME_TYPE' == "OAB"]) & (df['ACCOUNT_NO.'].str.contains("1121",case=False))
    ])
    df.drop(df[
        (df['SCHEME_TYPE' == "OAP"]) & (df['ACCOUNT_NO.'].str.contains("1121",case=False))
    ])

    df.to_csv('rawFile.csv')
    print("Irrelevant scheme types have been removed and account numbers containing 1121 have been saved.")

# Set empty maturity dates to tomorrows date
def emptyMaturity():
    tomorrow_datetime = datetime.now() + timedelta(days=1)
    
    df['MATURITY_DATE'].fillna(tomorrow_datetime.date(), inplace=True)
    df['MATURITY_DATE'] = pd.to_datetime(df['MATURITY_DATE'])
    df.to_csv('rawFile.csv')

    print("Empty Maturity_Date cells have been changed to tomorrows date.")