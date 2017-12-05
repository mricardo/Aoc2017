board = buckets = [[0 for col in range(10)] for row in range(10)]


def spiral(d, it, curr_it, y, x, v, target):
    while (v <= target):
        board[y][x] = board[y+1][x] + board[y+1][x-1] + board[y+1][x+1] + board[y][x-1] + board[y][x+1] + board[y-1][x] + board[y-1][x-1] + board[y-1][x+1]
        
        v = board[y][x]
        
        if (v > target):
            print('Solution:', v, end='\n\n')
            return
        
        
        if (d == 'R' and curr_it < it):
            curr_it += 1
            x+=1
        elif (d == 'R'):
            d = 'U'
            curr_it = 1
            y-=1    
        elif (d == 'U' and curr_it < it):
            curr_it+=1
            y-=1
        elif (d == 'U'):
            d = 'L'
            it += 1
            curr_it = 1
            x-=1
        elif (d == 'L' and curr_it < it):
            curr_it += 1
            x-=1        
        elif (d == 'L'):
            d = 'D'
            curr_it = 1
            y += 1   
        elif (d == 'D' and curr_it < it):
            curr_it += 1
            y += 1
        elif (d == 'D'):
            d = 'R'
            it += 1
            curr_it = 1
            x+=1            

x = len(board) // 2 - 1
y = len(board) // 2 - 1

board[y][x] = 1

spiral('R', 1, 1, y, x + 1, 2, 361527)

for x in board:
    for y in x:
        print (y, end='\t')
    print('\n')
