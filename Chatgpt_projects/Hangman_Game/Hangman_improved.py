import random


fruit_list = [

    "apple", "orange", "banana", "grape", "strawberry",
    "watermelon", "kiwi", "mango", "pineapple", "blueberry",
    "peach", "plum", "pear", "cherry", "raspberry",
    "blackberry", "lemon", "lime", "grapefruit", "pomegranate",
    "apricot", "nectarine", "cantaloupe", "honeydew", "avocado",
    "coconut", "papaya", "passionfruit", "guava", "fig",
    "date", "kiwifruit", "tangerine", "clementine", "persimmon",
    "dragonfruit", "elderberry", "cranberry", "gooseberry", "boysenberry",
    "starfruit", "jackfruit", "lychee", "blackcurrant", "redcurrant",
    "goji berry", "mulberry"
]

Lives = 10
Alive = True
random_word = random.choice(fruit_list)

print("The word is: " + random_word)

def hangmanPrinter():
    penalty = 10 - Lives

    a = "X "
    b = "_ "
    final = a * penalty + b * Lives
    print(final)


while Alive == True:
    guessing_word = input("\nGuess the fruit: ")

    if random_word != guessing_word:
        Lives -= 1
        
        print(str(Lives) + " Lives remaining")
        hangmanPrinter()

        if Lives == 0:
            print("Sorry YOU ARE DEAD LULW, THE CORRECT WORD WAS: " + random_word)
            Alive=False
    else:
        random_word == guessing_word
        print("well done! you have guessed the word with " + str(Lives) + " remaining")
        break
print("gg wp ")




# for i in ran


# need to find a way to do a more efficient way of showing 
# the amounts of lives instead of an entire if nested live