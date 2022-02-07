import random

'''Validate Function'''
#recieve user input
#return True if valid, False if invalid

def Validate(data):
    #check if data is numeric
    if data.isnumeric():
        data=int(data)
        #check data in range 1 to 10
        if data in range(1,11):
            return True
        else:
            print("Data must be a number between 1 and 10, inclusive")
            return False
    else:
        print("Data must be numeric")
        return False

#TEMPORARY TESTING
#check=Validate("11")
#print(check)


''' Main program'''
#generate a random number
number = random.randint(1,10)

#start game loop
while True:
    #get guess from user
    guess=input("Enter a number between 1 and 10")

    #if guess valid, play game
    if Validate(guess) == True:
        #print("Start Game")
        #convert guess to number
        guess = int(guess)
        #check if guess = number
        if guess == number:
            #output message "Correct!"
            print("Correct")
            break
        #break game loop

        #if guess < number
        elif guess < number:
            #output message "Too Low"
            print("Guess is too low!")

        #else
        else:
            #output message "Too High"
            print("Guess is too high!")

    else:
        #else, get another guess
        print("Guess not valid")


