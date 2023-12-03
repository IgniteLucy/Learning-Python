import random

# random_word_generation = random.randint(1,80)
#Version 1 of hangman
word_list = [
    "elephant", "computer", "rainbow", "library", "pineapple", 
    "galaxy", "adventure", "butterfly", "chocolate", "universe", 
    "waterfall", "happiness", "umbrella", "elephant", "fireplace", 
    "kangaroo", "treasure", "pineapple", "mountain", "elephant", 
    "keyboard", "happiness", "dragonfly", "cucumber", "pyramid", 
    "flamingo", "fireplace", "butterfly", "telephone", "zebra", 
    "adventure", "universe", "treasure", "elephant", "rainbow", 
    "keyboard", "happiness", "pineapple", "kangaroo", "mountain", 
    "chocolate", "umbrella", "waterfall", "library", "dragonfly", 
    "pyramid", "adventure", "universe", "treasure", "elephant", 
    "keyboard", "happiness", "pineapple", "kangaroo", "mountain", 
    "chocolate", "umbrella", "waterfall", "library", "dragonfly", 
    "pyramid", "flamingo", "fireplace", "butterfly", "telephone", 
    "zebra", "adventure", "universe", "treasure", "elephant", 
    "rainbow", "keyboard", "happiness", "pineapple", "kangaroo", 
    "mountain", "chocolate", "umbrella", "waterfall", "library"
]

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
print("tip, the word is " + random_word)


def hangmanPrinter():
    if Lives == 10:
        print("_ _ _ _ _ _ _ _ _ _ ")    
    elif Lives == 9:
        print("X _ _ _ _ _ _ _ _ _")
    elif Lives == 8:
        print("X X _ _ _ _ _ _ _ _")
    elif Lives == 7:
        print("X X X _ _ _ _ _ _ _")
    elif Lives == 6:
        print("X X X X _ _ _ _ _ _")
    elif Lives == 5:
        print("X X X X X _ _ _ _ _")
    elif Lives == 4:
        print("X X X X X X _ _ _ _")
    elif Lives == 3:
        print("X X X X X X X _ _ _")
    elif Lives == 2:
        print("X X X X X X X X _ _")
    elif Lives == 1:
        print("X X X X X X X X X _")
    elif Lives == 0:
        print("X X X X X X X X X X")

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
