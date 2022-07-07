import pandas as pd
from datetime import timedelta, datetime

def date():
    tomorrow_datetime = datetime.now() + timedelta(days=1)
    
    print(tomorrow_datetime.date())

date()