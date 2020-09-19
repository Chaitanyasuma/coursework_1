hosts = [["a", "1"],["b", "2"]]
with open('hosts', 'w') as h_csv:
  writer = csv.writer(h_csv)
  #writerow vs writerows
  writer.writerows(hosts)
