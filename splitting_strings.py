#set name variable
name="You like icecream and chocolate brownies"

print(name[0]) #prints Y
print(name[2]) #prints u
print(name[-1]) #prints last item in the array
print(name[:3]) #prints first 3 letters
print(name[9:31]) #prints "icecream and chocolate"

#split name into an array of words
words = name.split()

print(words) #prints the whole array
print(words[0]) #prints first word -  you
print(words[2]) #prints icecream
print(words[-1]) #prints last item in the array
print(words[:3]) #first three words
print(words[2:5]) #print words 3 to 5 - "icecream and chocolate"

#create an array using code
colours=["Red", "Green", "Blue", "Yellow"]

fav=input("What is your favourite colour?")
isColour=False

#print all the items in the array one at a time
for item in colours:
    if fav==item:
        isColour=True

if isColour == True:
    print("Colour was found.")
else:
    print("Colour not recognised.")
