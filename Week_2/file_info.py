os.path.getsize("filename")
os.path.getmtime("filename") #returns unix timestamp
#to make it more human readable
import datetime
timestamp = os.path.getmtime("filename")
datetime.datetime.fromtimestamp(timestamp)
os.path.abspath("filename")
