'''
Binary converter
This program converts a decimal number to a binary number.
'''

#get the number from from the user
decimal = input("Enter a number to convert to binary:")

#create a  BLANK str to hold the binary representation
binary = ""

#create a while loop that performs the calcs until the quotient is zero
while True:
    print(decimal)
    #get the quotient by dividing by 2
    quotient = int(decimal) /2

    #use modulo to get remainder
    remainder = int(decimal) % 2

    #print the
    print("Decimal:", str(decimal), "Quotient:", str(quotient), "Remainder:", str(remainder))

    #make the next decimal now equal to the quotient
    decimal = int(quotient)

    #create the binary string to hold the number
    binary = str(remainder) + binary

    #stop the calculation
    if int(quotient) == 0:
        print("Binary:", binary)
        break



