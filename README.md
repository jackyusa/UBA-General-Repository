# UBA-General-Repository

Automation of the Excel tasks through Python
* fix-raw-file
  * Updates the contents of the raw file
  * Removes irrelevant rows that dont belong to certain Scheme types
  * Removes certain OAP/OAB rows that dont contain 1121 in the Account Number
  * Sets empty Maturity dates to tomorrows date

* mci-mco
  * Sorts the maturity dates
