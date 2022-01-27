'''
Validation Algorithms
'''

'''#existence check
#checks whether the user has entered ANY data

#get data from user
data=input("Enter some data:")

if data == "":  
    print("No data has been entered")
else:
    #print data
    print(data)
'''

#data type check

number = input("Enter a number:")
#what are the rules for a number?
#0-9 digits - isnumeric()
#a single decimal point. count(.)==0

isnum=True
dp=0

for x in number:
        if x == ".":
            dp += 1
        else:
            if not x.isnumeric():
                isnum=False
                break

if isnum == True:
    if dp ==1: #convert to a float if theres a dot point
        number=float(number)
        print(type(number))
    elif dp == 0: #convert to an int
        number=int(number)
        print(type(number))
    else:
        print("Incorrect number of decimal points")
else:
    print("Number contains non numeric characters")

#range check
#"numeric ranges" ie between 1 and 10
age = input("Enter your age in years")

try:
    age=int(age)
    if age < 0 or age > 130:
        print("That is not a reasonable age for a human.")
    else:
        print("Age confirmed")
except:
    print("Not a valid integer.")

#"in a list" range - ie must be from a specific list
list = ["Apollo","Artemis","Athena","Poseidon"]

house=input("Which house are you in?")

if house not in list:
    print("Not a valid house")
else:
    print(house, "is valid")
'''

#keysborough e-mail validation algorithm
#example  BLY0014@keysboroughsc.vic.edu.au
#rules for a keysborough e-mail address:
#   first two characters are letters
#   third character is a letter of a "-"
#   next four characters are numbers
#   last part of the e-mail address is always "@keysboroughsc.vic.edu.au"

#get the user input
email = input("Enter your Keysborough e-mail address:")

#breaking up the string
print(email[0:3])
print(email[3:7])
print(email[7:])

#check each component and give feedback to the user if it has been incorrectly entered
if email[0:3].isalpha() and email[3:7].isnumeric() and email[7:] ==  "@keysboroughsc.vic.edu.au":
    print("E-mail valid")
else:
    print("Please enter a correct keysborough e-mail address")





















