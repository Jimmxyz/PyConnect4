try:
    import termcolor
    from termcolor import colored
    print("termcolor library imported sucessfuly")
    color_cli = True
except ImportError:
    print("termcolor failed to be imported")
    color_cli = False
turn = "X"
move = 0
grid = [
    ["0","1","2","3","4","5","6","7","8","9"],
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "]
]
def header():
    if color_cli == True:
        if turn == "X":
            print("[Connect 4] Move "+ str(move) + " ("+colored("X","red")+" turn)")
        elif turn == "O":
            print("[Connect 4] Move "+ str(move) + " ("+colored("O","blue")+" turn)")
    else:
        print("[Connect 4] Move "+ str(move) + " ("+turn+" turn)")
def gridPrint():
    for i in range(9):
        for j in range(10):
            if color_cli == True:
                if grid[i][j] == "X":
                    print("["+colored("X","red"), end="]")
                elif grid[i][j] == "O":
                    print("["+colored("O","blue"), end="]")
                elif grid[i][j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    print("["+colored(grid[i][j],"grey"), end="]")
                elif grid[i][j] == "!4":
                    print("["+colored("4","yellow"), end="]")
                else:
                    print("["+str(grid[i][j]), end="]")
            else:
                if grid[i][j] == "!4":
                    print("[4", end="]")
                else:
                    print("["+str(grid[i][j]), end="]")
        print()
def gameTurn():
    global move, turn
    header()
    gridPrint()
    if move == 0:
        print("Type the number of a row")
    moveID = input()
    if moveID == "e":
        print("Exiting PyConnect4...")
        return
    elif moveID not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if len(moveID) > 3:
            print(str(moveID[:3] + "... is not a valid number"))
            input()
            return gameTurn()
        else:
            print(str(moveID + " is not a valid number"))
            return gameTurn()
    else:
        emptySpaceFinder(int(moveID))
        if winCheck() == False:
            if turn == "X":
                turn = "O"
            elif turn == "O":
                turn = "X"
            move += 1
            return gameTurn()
def emptySpaceFinder(row):
    if grid[0][row] == "X" or grid[0][row] == "O":
        print("The row " + str(row) + " is full")
    else:
        for i in range(1,9):
            if grid[i][row] == "X" or grid[i][row] == "O":
                grid[i-1][row] = turn
                return
        grid[8][row] = turn
    return
def winCheck():
    x_streak = 0
    o_streak = 0
    for i in range(9):
        x_streak = 0
        o_streak = 0
        for j in range(10):
            if grid[i][j] == "X":
                x_streak += 1
                o_streak = 0
            elif grid[i][j] == "O":
                x_streak = 0
                o_streak += 1
            else:
                x_streak = 0
                o_streak = 0
            if x_streak == 4:
                win("X",i,i,j-3,j)
                return True
            elif o_streak == 4:
                win("O",i,i,j-3,j)
                return True
    x_streak = 0
    o_streak = 0
    for j in range(10):
        x_streak = 0
        o_streak = 0
        for i in range(9):
            if grid[i][j] == "X":
                x_streak += 1
                o_streak = 0
            elif grid[i][j] == "O":
                x_streak = 0
                o_streak += 1
            else:
                x_streak = 0
                o_streak = 0
            if x_streak == 4:
                win("X",i-3,i,j,j)
                return True
            elif o_streak == 4:
                win("O",i-3,i,j,j)
                return True
    rows = 9
    cols = 10
    for i in range(rows - 4 + 1):
        for j in range(cols - 4 + 1):
            x_streak = 0
            o_streak = 0
            for k in range(4):
                if grid[i+k][j+k] == "X":
                    x_streak += 1
                    o_streak = 0
                elif grid[i+k][j+k] == "O":
                    x_streak = 0
                    o_streak += 1
                else:
                    x_streak = 0
                    o_streak = 0
                if x_streak == 4:
                    win("X", i, i+k, j, j+k)
                    return True
                elif o_streak == 4:
                    win("O", i, i+k, j, j+k)
                    return True
    for i in range(4 - 1, rows):
        for j in range(cols - 4 + 1):
            x_streak = 0
            o_streak = 0
            for k in range(4):
                if grid[i-k][j+k] == "X":
                    x_streak += 1
                    o_streak = 0
                elif grid[i-k][j+k] == "O":
                    x_streak = 0
                    o_streak += 1
                else:
                    x_streak = 0
                    o_streak = 0
                if x_streak == 4:
                    win("X", i, i-k, j, j+k)
                    return True
                elif o_streak == 4:
                    win("O", i, i-k, j, j+k)
                    return True
    fulRow = 0
    for i in range(10):
        if grid[0][i] == 'X' or grid[0][i] == 'Y':
            fulRow += 1
    if fulRow == 10:
        gridPrint()
        print("Draw ! No empty place left")
        return True
    return False
def win(winner,lineStart,lineEnd,rowStart,rowEnd):
    grid[lineStart][rowStart] = "!4"
    grid[lineEnd][rowEnd] = "!4"
    lineSec = 0
    lineTrd = 0
    rowSec = 0
    rowTrd = 0
    if lineStart == lineEnd:
        lineSec = lineStart
        lineTrd = lineStart
    elif lineStart > lineEnd:
        lineSec = lineStart - 1
        lineTrd = lineStart - 2
    elif lineStart < lineEnd:
        lineSec = lineStart + 1
        lineTrd = lineStart + 2
    if rowStart == rowEnd:
        rowSec = rowStart
        rowTrd = rowStart 
    elif rowStart > rowEnd:
        rowSec = rowStart - 1
        rowTrd = rowStart - 2
    elif rowStart < rowEnd:
        rowSec = rowStart + 1
        rowTrd = rowStart + 2
    grid[lineSec][rowSec] = "!4"
    grid[lineTrd][rowTrd] = "!4"
    if color_cli == True:
        if winner == "X":
            print("[Connect 4] " + colored("X","red") + " is the " + colored("winner","yellow"))
        elif winner == "O":
            print("[Connect 4] " + colored("O","blue") + " is the " + colored("winner","yellow"))
    else:
        print("[Connect 4] " + winner + " is the winner")
    gridPrint()
    input()
    home()

def home():
    global turn, move, grid
    print("-------------------------------")
    print("          PyConnect 4          ")
    print("-------------------------------")
    print("")
    print("             V 1.1             ")
    print()
    print()
    print()
    print("     Press any key to start    ")
    input()
    turn = "X"
    move = 0
    grid = [
        ["0","1","2","3","4","5","6","7","8","9"],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "]
    ]
    gameTurn()
home()