
def sum(a, b, c):
    return a+b+c

def printBoard(xState, yState):

    zero = 'X' if xState[0] != 0 else ('O' if yState[0] != 0 else 0)
    one = 'X' if xState[1] != 0 else ('O' if yState[1] != 0 else 0)
    two = 'X' if xState[2] != 0 else ('O' if yState[2] != 0 else 0)
    three = 'X' if xState[3] != 0 else ('O' if yState[3] != 0 else 0)
    four = 'X' if xState[4] != 0 else ('O' if yState[4] != 0 else 0)
    five = 'X' if xState[5] != 0 else ('O' if yState[5] != 0 else 0)
    six = 'X' if xState[6] != 0 else ('O' if yState[6] != 0 else 0)
    seven = 'X' if xState[7] != 0 else ('O' if yState[7] != 0 else 0)
    eight= 'X' if xState[8] != 0 else ('O' if yState[8] != 0 else 0)

    print(f"{zero} | {one} | {two}")
    print("-----------")
    print(f"{three} | {four} | {five}")
    print("-----------")
    print(f"{six} | {seven} | {eight}")

    print("******************************************************")


def checkWin(state):
    winarr = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for wins in winarr:
        if sum(state[wins[0]] , state[wins[1]] , state[wins[2]]) == 3:
            return 1
    return 0


def main(): 
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1;
    print("Welcome to tic-tac-toe")
    turn=1  #1 for X and 0 for O
    printBoard(xState, yState)

    cnt = 0

    while True:
        if turn == 1:
            print("X's chance")
            cellno = int(input("Enter a cell no: "))
            # check if the cell is empty or not
            if xState[cellno] != 0 or yState[cellno] != 0:
                print("This cell is already filled, please enter another cell")
                continue
            xState[cellno] = 1
            printBoard(xState, yState)
            cnt = cnt+1
            if checkWin(xState) :
                print("X wins")
                print("Game over")
                break

        else:
            print("Y's chance")
            cellno = int(input("Enter a cell no: "))
            if xState[cellno] != 0 or yState[cellno] != 0:
                print("This cell is already filled, please enter another cell")
                continue
            yState[cellno]=1
            printBoard(xState,  yState)
            cnt = cnt+1
            if checkWin(yState) :
                print("X wins")
                print("Game over")
                break
        if cnt == 9:
            print("No one won, tie happened")
            break
        turn = 1 - turn




if __name__ == "__main__":
    main()