# What is this

Some tools to manage Gmail filters

# How to Use

1. Export Gmail filters
2. Convert the XML file to CSV
   ```console
   $ python convertFiltersToCSV.py mailFilters.xml
   ```
3. ...and back
   ```
   $ python convertCSVtoXML.py mailFilters.csv
   ```
