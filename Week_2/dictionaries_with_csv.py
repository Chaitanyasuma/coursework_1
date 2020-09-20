with open('filename') as sw:
  reader = csv.DictReader(sw)
  for row in reader:
    print(("{} has {} users").format(row["name"], row["users"])) # access columns like you access key values in a dictionary

# to write
with open('filename', 'w') as dept:
  writer = csv.DictWriter(filename, fieldnames = keys)
  writer.writeheader() # will create the first line of the CSV based on keys that we passed
  writer.writerows(dict_name) # will turn the list of dictionaries into lines in that file
