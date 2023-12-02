#Get inputs from users and use it

#*name = input("What is your name?")


action = input("what type of operation do you want to do? [ + OR - OR * OR / ]: ")
Number1 = input("Give me your first number: ")
Number2 = input("Give me your second number: ")


match action:
    case "+":
        print(float(Number1) + float(Number2))
    case "-":
        print(float(Number1) - float(Number2))
    case "*":
        print(float(Number1) * float(Number2))
    case "/":
        print(float(Number1) / float(Number2))       
    case _:
        print("DID you do something wrong homie?.. HUH?")







# IF YOU DO SOPMETING WRONG MAKE MOCKING NOISES
    

#print("Hello " + name + "!")


# animals = [
#     "lion",
#     "elephant",
#     "giraffe",
#     "zebra",
#     "tiger",
#     "penguin",
#     "koala",
#     "kangaroo",
#     "panda",
#     "cheetah",
#     "wolf",
#     "bear",
#     "rhinoceros",
#     "hippopotamus",
#     "monkey",
#     "gorilla",
#     "snake",
#     "crocodile",
#     "dolphin",
#     "whale",
#     "shark",
#     "octopus",
#     "elephant seal",
#     "polar bear",
#     "seagull",
#     "parrot",
#     "frog",
#     "turtle",
#     "butterfly",
#     "dalmatian"
# ]


# partA = animals[:17]
# partB = animals[17:]

# print(partA)
# print(partB)