
import random

def main():
    print("-welcome-")
    Menu()


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
        Quit()
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
            Quit()
        AdditionFocused(XVal, YVal)
    else:
        Addition()




def Division():
    DisplayMenu = """

    Division Flash Math


    """

    print(DisplayMenu)


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
        Quit()
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
            Quit()
        MultiplicationFocused(XVal, YVal)
    else:
        Addition()


def Subtraction():
    DisplayMenu = """

    Subtraction Flash Math

    """

    print(DisplayMenu)



def AdditionFlash(XVal, YVal):
    x = random.randint(0, XVal)
    y = random.randint(0, YVal)
    UserResponse = input("\n\n\n\n\n\n\n\n\n\n\n\n{} + {} = ? ".format(x, y))
    if UserResponse == "q":
        Quit()
    else:
        print("Answer = {}".format(x+y))
    UserResponse = input("")
    if UserResponse == "q":
        Quit()
    else:
        AdditionFlash(XVal, YVal)



def AdditionFocused(XVal, YVal):
    x = XVal
    y = random.randint(0, YVal)
    UserResponse = input("\n\n\n\n\n\n\n\n\n\n\n\n{} + {} = ? ".format(x, y))
    if UserResponse == "q":
        Quit()
    else:
        print("Answer = {}".format(x+y))
    UserResponse = input("")
    if UserResponse == "q":
        Quit()
    else:
        AdditionFocused(XVal, YVal)


def MultiplicationFlash(XVal, YVal):
    x = random.randint(0, XVal)
    y = random.randint(0, YVal)
    UserResponse = input("\n\n\n\n\n\n\n\n\n\n\n\n{} * {} = ? ".format(x, y))
    if UserResponse == "q":
        Quit()
    else:
        print("Answer = {}".format(x*y))
    UserResponse = input("")
    if UserResponse == "q":
        Quit()
    else:
        MultiplicationFlash(XVal, YVal)


def MultiplicationFocused(XVal, YVal):
    x = XVal
    y = random.randint(0, YVal)
    UserResponse = input("\n\n\n\n\n\n\n\n\n\n\n\n{} * {} = ? ".format(x, y))
    if UserResponse == "q":
        Quit()
    else:
        print("Answer = {}".format(x*y))
    UserResponse = input("")
    if UserResponse == "q":
        Quit()
    else:
        MultiplicationFocused(XVal, YVal)


def Quit():
    ByeMessage = "\n\nThank you for playing!"
    print(ByeMessage)
    exit()




if __name__ == main():
    print("starting flash math")
    main()
    print("flash math over")
