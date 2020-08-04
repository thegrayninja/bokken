
import random

def main():
    print("-welcome-")
    Menu()
    return 0


def Menu():
    DisplayMenu = """

    Welcome to Flash Math!


    Choose your Category:

        1. Addition
        2. Division
        3. Multiplication
        4. Subtraction


    To quit, enter "q" anytime during the program.

    """

    print(DisplayMenu)
    UserResponse = input(" > ")

    if UserResponse == "1":
        Addition()
    elif UserResponse == "2":
        Division()
    elif UserResponse == "3":
        Multiplication()
    elif UserResponse == "4":
        Subtraction()
    elif UserResponse.lower() == "q":
        Quit()
    else:
        Menu()
    return 0





def Addition():
    DisplayMenu = """
    \n\n\n\n\n\n\n\n\n\n\n\n
    Addition Flash Math


    Choose Your Game:

        1. Quick Addition - 10 max
        2. Quick Addition - 100 max
        3. Focused Addition

    """
    print(DisplayMenu)

    UserResponse = input(" > ")
    if UserResponse.lower() == "q":
        Menu()
    elif UserResponse == "1":
        AdditionFlash(10, 10)
    elif UserResponse == "2":
        AdditionFlash(100, 100)
    elif UserResponse == "3":
        try:
            XVal = int(input("Enter Static Number: "))
            YVal = int(input("Enter Maximum Range: "))
        except:
            print("Error: You must enter a number!")
            Addition()
        AdditionFocused(XVal, YVal)
    else:
        Addition()
    return 0




def Division():
    DisplayMenu = """

    Division Flash Math


    """

    print(DisplayMenu)
    Menu()
    return 0


def Multiplication():
    DisplayMenu = """
    \n\n\n\n\n\n\n\n\n\n\n\n
    Multiplication Flash Math


    Choose Your Game:

        1. Quick Multiplication - 12 max
        2. Challenge Multiplication - 100 max
        3. Focused Multiplication - customize numbers

    """
    print(DisplayMenu)

    UserResponse = input(" > ")
    if UserResponse.lower() == "q":
        Menu()
    elif UserResponse == "1":
        MultiplicationFlash(12, 12)
    elif UserResponse == "2":
        MultiplicationFlash(100, 100)
    elif UserResponse == "3":
        try:
            XVal = int(input("Enter Static Number: "))
            YVal = int(input("Enter Maximum Range: "))
        except:
            print("Error: You must enter a number!")
            Multiplication()
        MultiplicationFocused(XVal, YVal)
    else:
        Addition()
    return 0


def Subtraction():
    DisplayMenu = """

    Subtraction Flash Math

    Choose Your Game:

        1. Quick Subtraction - 12 max
        2. Challenge Subtraction - 100 max
        #3. Focused Subtraction - customize numbers

    """

    print(DisplayMenu)

    UserResponse = input(" > ")
    if UserResponse.lower() == "q":
        Menu()
    elif UserResponse == "1":
        SubtractionFlash(12, 12)
    elif UserResponse == "2":
        SubtractionFlash(100, 100)
    elif UserResponse == "3":
        try:
            XVal = int(input("Enter Static Number: "))
            YVal = int(input("Enter Maximum Range: "))
        except:
            print("Error: You must enter a number!")
            Menu()
        SubtractionFocused(XVal, YVal)
    else:
        Subtraction()
    return 0



def AdditionFlash(XVal, YVal):
    x = random.randint(0, XVal)
    y = random.randint(0, YVal)
    UserResponse = input("\n\n\n\n\n\n\n\n\n\n\n\n{} + {} = ? ".format(x, y))
    if UserResponse == "q":
        Addition()
    else:
        print("Answer = {}".format(x+y))
    UserResponse = input("")
    if UserResponse == "q":
        Addition()
    else:
        AdditionFlash(XVal, YVal)
    return 0



def AdditionFocused(XVal, YVal):
    x = XVal
    y = random.randint(0, YVal)
    UserResponse = input("\n\n\n\n\n\n\n\n\n\n\n\n{} + {} = ? ".format(x, y))
    if UserResponse == "q":
        Addition()
    else:
        print("Answer = {}".format(x+y))
    UserResponse = input("")
    if UserResponse == "q":
        Addition()
    else:
        AdditionFocused(XVal, YVal)
    return 0


def MultiplicationFlash(XVal, YVal):
    x = random.randint(0, XVal)
    y = random.randint(0, YVal)
    UserResponse = input("\n\n\n\n\n\n\n\n\n\n\n\n{} * {} = ? ".format(x, y))
    if UserResponse == "q":
        Multiplication()
    else:
        print("Answer = {}".format(x*y))
    UserResponse = input("")
    if UserResponse == "q":
        Multiplication()
    else:
        MultiplicationFlash(XVal, YVal)
    return 0


def MultiplicationFocused(XVal, YVal):
    x = XVal
    y = random.randint(0, YVal)
    UserResponse = input("\n\n\n\n\n\n\n\n\n\n\n\n{} * {} = ? ".format(x, y))
    if UserResponse == "q":
        Multiplication()
    else:
        print("Answer = {}".format(x*y))
    UserResponse = input("")
    if UserResponse == "q":
        Multiplication()
    else:
        MultiplicationFocused(XVal, YVal)
    return 0


def SubtractionFlash(XVal, YVal):
    x = random.randint(0, XVal)
    y = random.randint(0, YVal)

    if (x-y <0):
        SubtractionFlash(XVal, YVal)

    UserResponse = input("\n{} - {} = ? ".format(x, y))
    if UserResponse == "q":
        Subtraction()
    else:
        print("Answer = {}".format(x-y))
    UserResponse = input("")
    if UserResponse == "q":
        Subtraction()
    else:
        SubtractionFlash(XVal, YVal)
    return 0

def SubtractionFocused(XVal, YVal):
    x = XVal
    y = random.randint(0, YVal)
    if (y-x <0):
        SubtractionFocused(XVal, YVal)
    UserResponse = input("\n{} - {} = ? ".format(y, x))
    if UserResponse == "q":
        Subtraction()
    else:
        print("Answer = {}".format(x-y))
    UserResponse = input("")
    if UserResponse == "q":
        Subtraction()
    else:
        SubtractionFocused(XVal, YVal)
    return 0


def Quit():
    ByeMessage = "\n\nThank you for playing!"
    print(ByeMessage)
    exit()
    return 0




if __name__ == main():
    print("starting flash math")
    main()
    print("flash math over")
