from cmath import nan
import pandas as pd
from datetime import timedelta, datetime
import openpyxl

df = pd.read_csv('test.csv',index_col=0)

def date():
    tomorrow_datetime = datetime.now() + timedelta(days=1)
    
    print(tomorrow_datetime.date())

# test setting empty ones to 1 then changing them
def emptyMaturity():
    tomorrow_datetime = datetime.now() + timedelta(days=1)
    df['date'].fillna(tomorrow_datetime.date(), inplace=True)
    df["date"] = pd.to_datetime(df["date"])
    df.to_csv('test.csv')

    print("All empty Maturity dates have been set to tomorrows date.")

def removeRows():
    df.drop(df[
        (df.index != "jacky") &
        (df.index != "jason")].index, inplace=True)

    df['amount'] = df['amount'].apply(str)

    df.to_csv("test.csv")

emptyMaturity()