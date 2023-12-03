import random

Guessing = False
random_Number = random.randint(1,100)

Guesses = 0

#while Guessing == False():

while Guessing == False: # no need to be a function 

    guessed_Number = int(input("Guess the number: "))

    if(random_Number < guessed_Number):
        print("Lower")
        Guesses += 1
    elif(random_Number>guessed_Number):
        Guesses += 1
        print("Higher")
       
    else:
        print("guesed correctly!") 
        Guesses += 1
        Guessing = True

print("\ngame has finished, GG wp\nYou guessed the number after " + str(Guesses) + " Tries")

      




