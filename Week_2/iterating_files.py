with open("name") as file:
  for line in file:
    print(line.upper()) #creates newlines at the end, print adds a new one
#to avoid above
with open("name") as file:
  for line in file:
    print(line.strip().upper())


#to get file content in a list-like structure
file = open("name")
lines = file.readlines() #read all lines
file.close()
lines.sort()
print(lines)
