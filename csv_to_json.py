import csv
import json

# Open the CSV file and read in the data
csv_file = open('data.csv', 'r')
csv_reader = csv.DictReader(csv_file)

# Convert the data to a JSON object
json_data = []
for row in csv_reader:
    json_data.append(row)

# Write the JSON object to a file
json_file = open('data.json', 'w')
json.dump(json_data, json_file, indent=2)

# Close the files
csv_file.close()
json_file.close()
