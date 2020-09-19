import csv
f = open("filename")
csv_f = csv.reader(f)
for row in csv_f:
  #unpack
  n, p, r = row
  print("{}, {}, {}".format(n, p, r))
#alternative would be row[0]
f.close()
