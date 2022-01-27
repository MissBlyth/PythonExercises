# Type converer Algorithm
# integer  - 3, 21, 500  Only numbers
# float - 2.1  7.77777  0.98   numbers and a decimal point  5. 7876.827383872
# string/text  - "a. gdfghhgfd" "hello world" "I got 15 bucks!!!^&*@(!&#*!@("   any characters

# get data
data=input("Enter anything:")

# check if only numbers have been entered


dp=0 # checks for decimals
isnum = True #s tays true if only numbers

for x in data:
    # check if character is decimal point
    if x == ".":
        # count number of decimals
        dp += 1
    else:
        # check if character is NOT numeric
        if not x.isnumeric():
            # set isnum marker to false - there are non-numeric characters in the string
            isnum = False
            # stop the loop because non numeric chracters have been found, so not a number
            break

if dp == 0 and isnum == True:
    data=int(data)  # no decimals, only numbers = int
    print("Integer")

elif dp == 1 and isnum == True:
    data = float(data)
    print("Float")

else:
    print("Data is a string")


#check for decimal points - can only be ONEe









#get data from user
#assign the appropriate data type
