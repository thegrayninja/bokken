



def main():
    print("...main started...")

    Board, C1_Options, C2_Options, C3_Options, C4_Options = Setup()
    Pathways(Board, C1_Options, C2_Options, C3_Options, C4_Options)



def FactorMultiples(value):
    Total = 1
    for i in range(1, int(value)+1):
        Total *= i
    return Total



def Setup():
    Board = {
        "C1": "b",
        "C2": "a",
        "C3": "r",
        "C4": "n",
    }


    C1_Options = {
        "C2": Board["C2"],
        "C3": Board["C3"],
        "C4": Board["C4"]
    }

    C2_Options = {
        "C3": Board["C4"],
        "C1": Board["C1"],
        "C4": Board["C3"]
    }

    C3_Options = {
        "C1": Board["C1"],
        "C2": Board["C2"],
        "C4": Board["C4"]
    }

    C4_Options = {
        "C1": Board["C1"],
        "C2": Board["C2"],
        "C3": Board["C3"]
    }



    return Board, C1_Options, C2_Options, C3_Options, C4_Options

    # for key, value in Board.items():
    #     print(key)
    #     print(value)
    #     print("\n--\n")


def Pathways(Board, C1_Options, C2_Options, C3_Options, C4_Options):
    UsedWords = []
    UsedPaths = []
    Factors = FactorMultiples(4)
    print(Factors)
    Count = 0

    #while Count < Factors:
    while Count < 5:
        UsedCells = []
        for key, value in Board.items():
            # InitialChar = value
            # InitialCell = key
            TempWord = ""
            if key not in UsedCells:
                #TempWord += value
                UsedCells.append(key)
                print("first wave - {}".format(key))

                #NewPath = "1"
                while key != "0":
                    if key == "C1":
                        UsedCells.append(key)
                        TempWord += Board[key]

                        if "C2" not in UsedCells:
                            UsedCells.append("C2")
                            print("ok,did somethign in C1")
                            key = "C2"

                        elif "C4" not in UsedCells:
                            UsedCells.append("C4")
                            print("ok,did somethign in C1")
                            key = "C4"

                        elif "C3" not in UsedCells:
                            UsedCells.append("C4")
                            print("ok,did somethign in C1")
                            key = "C3"
                        else:
                            key = "0"



                        # #for key, value in C1_Options.items():
                        # print(key)
                        # if key not in UsedCells:
                        #
                        #     print(value)
                        #     #key = C2_Paths(TempWord, UsedCells, Board)
                        #     if "C4" not in UsedCells:
                        #         UsedCells.append("C4")
                        #         print("ok,did somethign in C2")
                        #         key = "C4"
                        #     else:
                        #         key = "0"

                    elif key == "C2":
                        UsedCells.append(key)
                        TempWord += Board[key]

                        if "C1" not in UsedCells:
                            UsedCells.append("C1")
                            print("ok,did somethign in C1")
                            key = "C1"

                        elif "C4" not in UsedCells:
                            UsedCells.append("C4")
                            print("ok,did somethign in C1")
                            key = "C4"

                        elif "C3" not in UsedCells:
                            UsedCells.append("C3")
                            print("ok,did somethign in C1")
                            key = "C3"
                        else:
                            key = "0"
                        # for key, value in C2_Options.items():
                        #     if key not in UsedCells:
                        #         UsedCells.append(key)
                        #         TempWord += value
                        #         print(value)
                    elif key == "C3":
                        UsedCells.append(key)
                        TempWord += Board[key]

                        if "C1" not in UsedCells:
                            UsedCells.append("C2")
                            print("ok,did somethign in C1")
                            key = "C1"

                        elif "C4" not in UsedCells:
                            UsedCells.append("C4")
                            print("ok,did somethign in C1")
                            key = "C4"

                        elif "C2" not in UsedCells:
                            UsedCells.append("C2")
                            print("ok,did somethign in C1")
                            key = "C2"
                        else:
                            key = "0"

                    elif key == "C4":
                        UsedCells.append(key)
                        TempWord += Board[key]

                        if "C1" not in UsedCells:
                            UsedCells.append("C2")
                            print("ok,did somethign in C1")
                            key = "C1"

                        elif "C2" not in UsedCells:
                            UsedCells.append("C2")
                            print("ok,did somethign in C1")
                            key = "C2"

                        elif "C3" not in UsedCells:
                            UsedCells.append("C4")
                            print("ok,did somethign in C1")
                            key = "C3"
                        else:
                            key = "0"
                    else:
                        key = "0"
            if TempWord != "":
                UsedWords.append(TempWord)
        UsedPaths.append(UsedCells)
        Count += 1
        #print(UsedCells)
    print(UsedWords)
    for i in UsedPaths:
        #print(UsedPaths)
        print(i)


def C1_Paths(TempWord, UsedCells, Board):
    C1_Options = {
        "C2": Board["C2"],
        "C3": Board["C3"],
        "C4": Board["C4"]
    }

    for key, items in C1_Options.items():
        if key not in UsedCells:
            UsedCells.append(TempWord)
            return key
        else:
            return "0"


def C2_Paths(TempWord, UsedCells, Board):
    C2_Options = {
        "C1": Board["C1"],
        "C4": Board["C4"],
        "C3": Board["C3"]
    }
    print("yes, got into C2_Paths")

    if "C1" not in UsedCells:
        UsedCells.append("C1")
        print("ok,did somethign in C2")
        return "C1"

    elif "C4" not in UsedCells:
        UsedCells.append("C4")
        print("ok,did somethign in C2")
        return "C4"

    elif "C3" not in UsedCells:
        UsedCells.append("C4")
        print("ok,did somethign in C2")
        return "C3"

    print("printing a key value of 0")
    return "0"

def C3_Paths(TempWord, UsedCells, Board):
    C3_Options = {
        "C1": Board["C1"],
        "C2": Board["C2"],
        "C4": Board["C4"]
    }
    for key, items in C3_Options.items():
        if key not in UsedCells:
            UsedCells.append(TempWord)
            return key
        else:
            return "0"

def C4_Paths(TempWord, UsedCells, Board):
    C4_Options = {
        "C1": Board["C1"],
        "C2": Board["C2"],
        "C3": Board["C3"]
    }
    for key, items in C4_Options.items():
        if key not in UsedCells:
            UsedCells.append(TempWord)
            return key
        else:
            return "0"

        # for key, value in C1_Options.items():
        #     print("second wave - {}".format(key))
        #     TempWord = ""
        #     TempWord += InitialChar
        #     UsedSquares = []
        #     UsedSquares.append(InitialChar)
        #     if key not in UsedSquares:
        #         if len(TempWord) < 3:
        #             UsedSquares.append(key)
        #             TempWord += value
        #         else:
        #             UsedWords.append(TempWord)
        #
        # print(TempWord)
        # print(UsedSquares)
        # print(UsedWords)







if __name__ == "__main__":
    main()
    print("goodbye")