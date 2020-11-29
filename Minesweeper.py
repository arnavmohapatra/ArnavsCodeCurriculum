import  random

board = []
for x in range(9):
    board.append([])
    for _ in range(9):
        board[x].append("[█]")

def printBoard():
    for x in range(9):
        for y in range(9):
            print(board[x][y], end="")
        print("   "+str(x+1))
    print()
    for x in range(9):
        print(" "+str(x+1)+" ", end="")
    print()

difficulty = input("Which difficulty level? (easy, medium, hard): \n")
while (not (difficulty=="easy" or difficulty=="medium" or difficulty=="hard")):
    print("Invalid input for difficulty, try again")
    difficulty = input("Which difficulty level? (easy, medium, hard): \n")
mine_rate = {"easy":9, "medium":4, "hard":2} #rates are equivalent to 1/n (.11, .25, .5)

printBoard()
 
print("Select the first box")
xi, yi = int(input("Enter X coordinate:\n")), int(input("Enter Y coordinate:\n")) 
while(xi<0 or xi>8 or yi<0 or yi>8):
    print("Invalid input for either X or Y, try again")
    xi, yi = int(input("Enter X coordinate:\n")), int(input("Enter Y coordinate:\n")) 

for x in range(9):
    for y in range(9):
        board[x][y]="[0]"

for x in range(9):
    for y in range(9):
        if(random.randint(0,mine_rate[difficulty])==0):
            board[x][y] = "[x]"

for a in range(-1,2):
    for b in range(-1,2):
        if(xi+a<0 or xi+a>8 or yi+b<0 or yi+b>8):
            continue
        board[xi+a][yi+b]="[0]"


for x in range(9):
    for y in range(9):
        for a in range(-1,2):
            for b in range(-1,2):
                if(x+a<0 or x+a>8 or y+b<0 or y+b>8):
                    continue
                if(board[x][y]=="[x]"):
                    continue
                if(board[x+a][y+b]=="[x]"):
                    board[x][y] = "["+str(int(board[x][y][1])+1)+"]"

for x in range(9):
    for y in range(9):
        if(board[x][y]=="[0]"):
            board[x][y] = "[ ]"

printBoard()
                    
