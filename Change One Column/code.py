
# This code takes in an input csv file and places the text in the first column into apostrophes and a comma at the end
# Rename the initial/original csv file to "input" and make sure it is a "CSV (Comma deliminted) (*.csv)"
# Place the file into the folder and when prompted if you want to replace the other input.csv file click yes
# Then double click the code file and the output will be in the output file
# If double clicking it opens Visual Studios, python hasn't been downloaded or set to the default app
# Right click the code.py file and hover over the "Open With" then click python
# Can still just click the run icon ( play icon ) on visual studios in the code.py file on the top left

import pandas as pd
import numpy as np

df = pd.read_csv('input.csv', index_col=0)

def addChar():
    
    df.index = "'" + df.index + "'" + ","
    df.to_csv('output.csv')
    

addChar()
