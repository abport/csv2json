# CSV to JSON Converter
Python Script that Converts a CSV file to a JSON file

This script assumes that the .csv file has a header row with field names. 

Here is a sample .csv file that you can use with the script:

    Name,Age,Gender
    Alice,25,Female
    Bob,30,Male
    Charlie,35,Male

This .csv file has three rows and three columns, with the first row containing field names.

The JSON file will contain an array of objects, with each object representing a row in the .csv file and the field names as the keys.

 When converted to a .json file using the script above, it will look like this:

```json
[  {    "Name": "Alice",    "Age": "25",    "Gender": "Female"  },  {    "Name": "Bob",    "Age": "30",    "Gender": "Male"  },  {    "Name": "Charlie",    "Age": "35",    "Gender": "Male"  }]
```
Each object in the array represents a row in the .csv file, and the field names are used as keys in the JSON object.

To use this script, simply replace 'data.csv' and 'data.json' with the names of your input and output files, respectively. You can then run the script using a Python interpreter.

For example, you could use the following command to run the script:
```python
python csv_to_json.py
```
This will convert the .csv file to a .json file, and write the resulting JSON data to the output file.
