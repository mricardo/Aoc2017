from Day10 import knot_hash

def to_binary(input):
    b = []      
    for l in input:
        b.extend([int(x) for x in bin(int(l, 16))[2:].zfill(4)])
    
    return b

def floodfill(disk, x, y, group):    
    if disk[x][y] == 1:  
        disk[x][y] = group        
    
        if x > 0:
            floodfill(disk, x - 1, y, group)

        if x < len(disk[y]) - 1:
            floodfill(disk, x + 1, y, group)

        if y > 0:
            floodfill(disk, x, y - 1, group)

        if y < len(disk) - 1:
            floodfill(disk, x, y + 1, group)
    
def calculate_region(disk, group, i, j):
    group = 1
    for x, row in enumerate(disk):
        for y, cell in enumerate(row):
            if (cell == 1):                 
                group += 1
                floodfill(disk, x, y, group)                 

    return group - 1

def calculate_fills_and_region(key):
    fills = 0
    disk = []
    for i in range(0, 128):
        b = to_binary(knot_hash(key + str(i)))
        disk.append(b)
        fills += b.count(1)

    print(fills)    
    print(calculate_region(disk, 0, 0, 0))

calculate_fills_and_region("nbysizxe-")
# 128 knot hash