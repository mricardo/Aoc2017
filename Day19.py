
def walk_through(m, max_x, max_y):
    y = 0
    x = m[y].index('|')
    d = 'd'
    visited_letters =  []
    steps = 0
    last_step = 0
    while True:
        if (y < 0 or x < 0):
            break
        steps += 1  
        path = m[y][x]
        
        if (path not in visited_letters and path.isalpha()):
            visited_letters.append(path)
            last_step = steps

        if ((d == 'd' or d == 'u') and (path != '+')):
            y = (y + 1 if d == 'd' else y - 1)          
        elif ((d == 'l' or d == 'r') and (path != '+')):
            x = (x + 1 if d == 'r' else x - 1)
        elif (path == '+'):
            if (d == 'd' or d == 'u'):
                if ((x - 1 >= 0) and ((m[y][x-1] == '-') or m[y][x-1].isalpha())):
                    d = 'l'
                    x -= 1
                elif ((x + 1 < max_x) and ((m[y][x+1] == '-') or m[y][x+1].isalpha())):
                    d = 'r'
                    x += 1
            elif (d == 'l' or d == 'r'):
                if ((y + 1 < max_y) and ((m[y+1][x] == '|') or m[y+1][x].isalpha())):
                    d = 'd'
                    y += 1
                elif ((y - 1 >= 0) and ((m[y-1][x] == '|') or m[y-1][x].isalpha())):
                    d = 'u'
                    y -= 1
        else:
            break      
  
        
    print ("Steps: ", last_step)
    return ''.join(visited_letters)

def read_map():    
    with open("input") as f:
        return f.read().splitlines()    

m = read_map()
print(walk_through(m, len(m[0]), len(m)))
