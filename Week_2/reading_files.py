file = open("name")
print(file.readline())
print(file.read()) #starts from wherever we are currently to EOF
file.close() #limited number of file descriptors that you can create
#python lets us automatically close a file
with open("name") as file:
  print(file.readline())
