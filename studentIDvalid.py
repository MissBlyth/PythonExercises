# ask student ID
studentId = input("Enter a student ID:")

#check that something has been entered.
if studentId == "":
    print("No data entered")

#check string length
idLength= len(studentId)

if idLength != 7:
    print("Incorrect number of characters.")

else:
    #split the string
    firstThree = studentId[:3]
    print("First three letters:", firstThree)

    lastFour = studentId[3:]
    print("Last three letters:", lastFour)

#check if the first three characters are letters
    if firstThree.isalpha():
        print("First three are alpha")
    else:
        print("First three are NOT alpha - enter a valid ID")

#check if the last 4 are numbers
    if lastFour.isnumeric():
        print("Last four are numeric")
    else:
        print("Last four are NOT alpha - enter a valid ID")


