board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def print_board(bo):
    for i in range(len(bo)):
        if (i % 3 == 0) and i != 0:
            print("-------------------------")
        for j in range(len(bo[0])):
            if (j % 3 == 0) and j != 0:
                print(" | ",end=" ")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+ " ",end="")

def find_empty(bo,l):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False            
                
def is_safe(board,row,col,num):
    for i in range(0,9):
        if board[row][i] == num:
            return False    
    for i in range(0,9):
        if board[i][col] == num:
            return False 
    row = row - (row % 3)
    col = col - (col%3)              
    for i in range(3):
        for j in range(3):
            if(board[i+row][j+col]==num):
                return False
    return True            

def sudokuSolver(board):
    l = [0,0]

    if(not(find_empty(board,l))):
        return True
    row = l[0]
    col = l[1]

    for num in range(1,10):
        if is_safe(board,row,col,num):
            board[row][col] = num

            if sudokuSolver(board):
                return True
            board[row][col] = 0
    return False        


sudokuSolver(board)
print_board(board)          



