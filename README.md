# UBA-General-Repository

Automation of the Excel tasks through Python
* **fixRaw.py**
  * removeRows()
    * Filters the file for only scheme types belonging to - ODA/CAA/LAA/OAP/OAB.
    * Saves rows belonging to OAB/OAP where the account number contains 1121 while filtering out the rest.
  * emptyMaturity()
    * Sets empty maturity date cells to tomorrow's date.
    * Tomorrow's date will always update to the next date using the pandas datetime functions.
  * sortByMaturity()
    * Sorts the dataframe(file) based on the maturity date in ascending order.
  * addAmountColumn()
    * Adds a column called "AMOUNT" and has the values of CLS_BALANCE that are negated.
  * insertColumn(columnName, index, values)
    * Takes a :
        * *columnName* = what you want to call the column
        * *index* = where you want the column to go in the dataframe
        * *values* = what you want it's values to be
  * convertToUSD()
    * Adds a column called USD_AMOUNT that contains the Amounts converted to USD through conversion rates.
  * *fixFile()*
    * The conclusive function that calls all prior functions in the file. Results in the finished file.
* **mci_mco.py**
  * addRow()
    * Adds a row with certain columns to the dataframe.
  * sortMaturity()
    * Sorts the dataframe by the maturity date in ascending order.

* **merge_files.py**
