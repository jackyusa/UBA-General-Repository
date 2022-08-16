
# This code takes in a names csv file and creates files that contain a name for each count
# The code takes template.csv as the template for each of the files created
# Rename the initial/original csv file containing the names to "names" and make sure it is a "CSV (Comma deliminted) (*.csv)"
# Place the file into the folder and when prompted if you want to replace the other names.csv file click yes
# Then double click the code file and the files will be created into the same folder
# If double clicking it opens Visual Studios, python hasn't been downloaded or set to the default app.
# Right click the main.py file and hover over the "Open With" then click python
# Can still just click the run icon ( play icon ) on visual studios in the main.py file on the top left.

from contextlib import nullcontext
from re import A
import pandas as pd
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt

template = pd.read_csv("template.csv")
#names = pd.read_csv("names.csv", index_col=0)

namesList = ['jacky','danny','david','sam','james','daniel']

for i in range(0,len(namesList)):
    #change line 8 and 18 in template to the name
    template.loc[6,'Message']=namesList[i]
    template.loc[16,'Message']=namesList[i]

    template.to_csv("C:/Users/lija/Documents/CyberSecurityFiles/Check Audit Names/files" + str(i) + ".csv",index=False)