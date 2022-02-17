'''
This program calculates how many days until the next christmas
IT DOES NOT WORK NEXT YEAR or after christmas
'''

#get the date time library
import datetime

#get current date
today = datetime.datetime.now()
print(today.year)

#set christmas date
christmas = datetime.datetime(2022,12,25)
print(christmas)

#how long til christmas
print(christmas - today)
