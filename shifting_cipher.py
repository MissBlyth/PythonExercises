
#create array of letters
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#get message to be shifted from the user
message=input("Enter your name:")


message = message.lower()

shift=input("How much would you like to shift the message:")

for x in message:
    if x.isalpha()==True:
        position = letters.index(x)
        position = position + int(shift)
        if position  > 25:
            position = position - 26
        print(letters[position])
    else:
        print(x)
