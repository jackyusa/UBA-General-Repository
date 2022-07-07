import pandas as pd
import numpy as np
from datetime import timedelta, datetime

df = pd.read_csv('rawFile.csv',index_col=0)

# Remove rows that are not ODA/CAA/LAA or OAB/OAP that
# the account number doesn't have 1121 in the 7th place
def removeRows():
    # First filter out those that aren't ODA/CAA/LAA/OAP/OAB
    df.drop(df[
        (df.SCHEME_TYPE != "ODA") &
        (df.SCHEME_TYPE != "CAA") &
        (df.SCHEME_TYPE != "LAA") &
        (df.SCHEME_TYPE != "OAP") &
        (df.SCHEME_TYPE != "OAB")].index, inplace=True)
    
    # Find where rows are OAB/OAP and dont have 1121 in the
    # account number and set the account number to "1" then
    # go through the rows again and delete rows that have "1"
    df.loc[df['ACCOUNT_NO.'.find('1121') != -1], 'ACCOUNT_NO.'] = 1
    df.drop(df['ACCOUNT_NO.' == 1].index, inplace=True)

    df.to_csv('rawFile.csv')

# Set empty maturity dates to tomorrows date
def emptyMaturity():
    tomorrow_datetime = datetime.now() + timedelta(days=1)
    replaced = df['MATURITY_DATE'].replace('',tomorrow_datetime.date())

    replaced.to_csv('rawFile.csv')