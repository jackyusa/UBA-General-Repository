# **UBA General Repository**

## Code Files:
###### To run the codes on Visual Studios if double clicking the file doesn't work the whole folder needs to be opened. Open Visual Studios -> Click File -> Open Folder -> Click the File and Click Select Folder.
```
Add Apostrophes and Comma
- The code takes in an input csv file and places the text in the first column into apostrophes and a comma at the end.
- Rename the initial/original csv file to "input" and make sure it is a "CSV (Comma deliminted) (*.csv)".
- Place the file into the folder and when prompted if you want to replace the other input.csv file click yes.
- Then double click the code file and the output will be in the output file.
- If double clicking it opens Visual Studios, python hasn't been downloaded or set to the default app.
- Right click the code.py file and hover over the "Open With" then click python.
- Can still just click the run icon ( play icon ) on visual studios in the code.py file on the top left.
```

```
Check Audit Names
- The code takes in a names csv file and creates files that contain a name for each count.
- The code takes template.csv as the template for each of the files created.
- Rename the initial/original csv file containing the names to "names" and make sure it is 
- a "CSV (Comma deliminted) (*.csv)".
- Place the file into the folder and when prompted if you want to replace the other names.csv file click yes.
- Then double click the code file and the files will be created into the same folder.
- If double clicking it opens Visual Studios, python hasn't been downloaded or set to the default app.
- Right click the main.py file and hover over the "Open With" then click python.
- Can still just click the run icon ( play icon ) on visual studios in the main.py file on the top left.
```

```
MCI-MCO Report
- The code takes in two input csv files - "inputRawFile" and "inputBlotterFile".
- inputRawFile contains the data that will be manipulated and filtered.
- Specifics:
   * fixInputFile.py removes multiple columns then removes rows where the scheme type is not the needed types.
   * fixInputFile.py then finds rows where OAB/OAP dont have 1121 in the account number and remove them.
   * fixInputFile.py then adds an AMOUNT and USD_AMOUNT column. AMOUNT being a copy of CLS_BALANCE column but
   * the values are negated. USD_AMOUNT being the AMOUNT column with its values converted based on the
   * currency type in the CRNCY column. The currency is converted using a currency API that is requested on
   * the top of the file. The request returns a dictionary that contains the currency type as the key with
   * the value being the currency conversion rate.
   * fixInputFile.py also sets empty and old Maturity Dates to tomorrows date.
   * fixInputFile.py then inserts the DDA rows containing the unique date and sum.
   * fixInputFile.py finally deltes the CAA and ODA rows and sorts the data rows based on the MATURITY_DATE.
   ----------------------------------------------------------------------------------------------------------
   * fixBlotterFile.py renames many of the columns that are the same in inputRawFile to merge the two files.
   * fixBlotterFile.py calls fixInputFile.py which gets the return file for the InputRawFile.
   * fixBlotterFile.py then removes all the columns except the Maturity Date and USD Amounts.
   * fixBlotterFile.py then sets the format for the dates and sorts them.
- The file is then combined with inputBlotterFile.
- The final output file contains only the two columns with the Maturity dates sorted and the USD Amounts.
- To use the code just replace inputRawFile and inputBlotterFile with the respective csv files.
- Then run the fixBlotterFile.py code with the same process as the other codes.
```

```
Top Hits
- This code takes in an input csv file and for each matches row, it splits the data points into their own row and
- splits the Match and their information into two different columns. The code also gives the count of the matches
- in a separate column and saves the data in the outputs files and displays a bar graph of the top x number of
- matches ( this can be changed by changing the number in line 51 of the code "dfFinal = df2.head(20)". In this
- case 20 would return the top 20.
- Rename the initial/original csv file to "input" and make sure it is a "CSV (Comma deliminted) (*.csv)".
- Then double click the code file and the output files will be updates with the results.
- If double clicking it opens Visual Studios, python hasn't been downloaded or set to the default app.
- Right click the main.py file and hover over the "Open With" then click python
- Can still just click the run icon ( play icon ) on visual studios in the main.py file on the top left.
- output 1 - contains the Matches and MatchesSplit
- output 2 - contains the columns with their counts without duplicates
- output 3 - contains the top x number of the counts
- To change the display of the graph simply adjust the settings of the graph by clicking the configure icon.
```
