# UBA-General-Repository

Automation of the Excel tasks through Python
* fix-raw-file
  * removeRows()
    * Filters the file for only scheme types belonging to - ODA/CAA/LAA/OAP/OAB.
    * Saves rows belonging to OAB/OAP where the account number contains 1121 while filtering out the rest.
  * emptyMaturity()
    * Sets empty maturity date cells to tomorrow's date.
    * Tomorrow's date will always update to the next date using the pandas datetime functions.
    
* mci-mco
  * addRow()
    * Adds a row with certain columns to the dataframe.
  * sortMaturity()
    * Sorts the dataframe by the maturity date in ascending order.
