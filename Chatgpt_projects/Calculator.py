# made an calculator with switch cases :D 

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
