

grid = [[0,0,0],[0,0,0],[0,0,0]]

def get_state(grid,row,col):
    occupant = grid[col-1][row-2]
    if occupant == 1:
        return "X"
    if occupant == 2:
        return "O"
    return " "

def set_state(grid,row,col,player):
    if player == "X":
        occupant = 1
    else:
        occupant = 2
    grid[col-1][row-1] = occupant

def is_winner(grid):
    if grid[1][1] != 0:
        if grid[0][0] == grid[1][1]:
            if grid[2][2] == grid[1][1]:
                return True
        if grid[2][0] == grid[1][1]:
            if grid[0][2] == grid[1][1]:
                return True
    for i in xrange(0,3):
        if grid[0][i] != 0:
            if grid[0][i] == grid[1][i]:
                if grid[0][i] == grid[2][i]:
                    return True
        if grid[i][0] != 0:
            if grid[i][0] == grid[i][1]:
                if grid[i][0] == grid[i][2]:
                    return True
    return False

def print_grid(grid):
    print_row(grid, 1)
    print "---------"
    print_row(grid, 2)
    print "---------"
    print_row(grid, 3)

def print_row(grid, row):
    output = get_state(grid,row,1)
    output += " | " + get_state(grid,row,2)
    output += " | " + get_state(grid,row,3)
    print output




ongoing = True
current_player = "X"
spaces = 9
while ongoing:
    print_grid(grid)
    print current_player + "'s turn"
    print "Column?"
    col = int(raw_input())
    print "Row?"
    row = int(raw_input())
    current = get_state(grid,row,col)
    if current != " ":
        print "that space is occupiced"
    else:
        set_state(grid,row,col, current_player)
        spaces -= 1

        if is_winner(grid):
            print "winner is: "+ current_player
            ongoing = False
        else:
            if current_player == 'X':
                current_player = "O"
            else:
                current_player = "X"


        if spaces == 0:
            print "end"
            ongoing = False

