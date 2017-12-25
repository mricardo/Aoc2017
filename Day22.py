total_bursts = 0
def turn(x, y, curr_d, next_d):
    if (curr_d == 'u'):
        if (next_d == 'l'):
            return (x-1, y, 'l')
        if (next_d == 'r'):
            return (x+1, y, 'r')
    
    if (curr_d == 'd'):
        if (next_d == 'l'):
            return (x+1, y, 'r')
        if (next_d == 'r'):
            return (x-1, y, 'l')

    if (curr_d == 'l'):
        if (next_d == 'l'):
            return (x, y+1, 'd')
        if (next_d == 'r'):
            return (x, y-1, 'u')

    if (curr_d == 'r'):
        if (next_d == 'l'):
            return (x, y-1, 'u')
        if (next_d == 'r'):
            return (x, y+1, 'd')

def burst(memory, grid, activity):
    global total_bursts
    d = 'u'

    y = len(grid) // 2
    x = len(grid) // 2
    i = 0
    while i < activity:
        cell = get_cell(memory, grid, y, x)
        if (cell == '#'):
            set_cell(memory, grid, y, x, '.')
            (x, y, d) = turn(x, y, d, 'r')            
        else:
            set_cell(memory, grid,  y, x, '#')
            (x, y, d) = turn(x, y, d, 'l')
            total_bursts += 1                   
        i += 1

def get_cell(memory, grid, y, x):
    if (y,x) not in memory:
        if (y >= len(grid) or x >= len(grid) or y < 0 or x < 0):           
            memory[(y,x)] = '.'
        else:
            memory[(y,x)] = grid[y][x] 
    return memory[(y,x)]

def set_cell(memory, grid, y, x, val):
    memory[(y,x)] = val
    if (not (y >= len(grid) or x >= len(grid) or y < 0 or x < 0)):
        grid[y] = grid[y][:x] + val + grid[y][x+1:]

def read():
    with open("input") as f:
        grid = [line.rstrip() for line in f]
    return grid

grid = read()
memory = {}

burst(memory, grid, 10000)
print(total_bursts)

