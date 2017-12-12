import re

adjacency_matrix = [[0 for x in range(2000)] for y in range(2000)]
processed = [0 for x in range(2000)]

def add_connection(x, y):
    adjacency_matrix[x][x] = 1
    adjacency_matrix[y][y] = 1
    adjacency_matrix[x][y] = 1

def find_connections(x, y):
    
    if (adjacency_matrix[x][y] == 1):
        processed[x] = 1
        total = 0
          
        for i, v in enumerate(adjacency_matrix[x]):            
            if (v and i != y and not processed[i]):
                total += find_connections(i, i)

        return 1 + total
    return 0     

def find_groups():
    groups = 0
    for i, x in enumerate(processed):        
        if (not x):
            if (find_connections(i,i)):
                groups +=1
    return groups
          

def read():
    pattern = re.compile('^(\d+)\s(?:<->)\s(\d+(,\s\d+)*)$')    
   
    with open('input') as f:        
        for line in f:
            m = pattern.match(line)
            if (m != None):         
                v = int(m.group(1))
                neighbours = [int(x) for x in m.group(2).split(', ')]
                for n in neighbours:
                    add_connection(v, n)

read()      
print(find_connections(0, 0))
processed = [0 for x in range(2000)]
print(find_groups())