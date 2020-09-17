import os
os.remove("filename")
#FileNotFoundError is file doesn't exist
os.rename("prev", "new")
#sub-module to check whether file exists
os.path.exists("filename") #returns True or False
