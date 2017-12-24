import re

def hash(pattern):
    l = []
    for i, p in enumerate(pattern):
        l.extend("".join(p))
        if (i + 1 < len(pattern)):
            l.extend("/")

    return "".join(l)

def flip (pattern):
    aMatrix = pattern.split("/")
    flipped = []
    for p in aMatrix:
        flipped.append(p[::-1])

    return hash(flipped)

def convert(pattern):
    return pattern.split("/")

def rotate(pattern):
    aMatrix = pattern.split("/")
    return flip(hash(list(map(list, zip(*aMatrix)))))

def find_rule(rules, pattern):
    for i in range(4):
        if pattern in rules:
            return rules[pattern]
                
        flipped = flip(pattern)
        if (flipped in rules):
            return rules[flipped]

        pattern = rotate(pattern)               

    return None
    
def read():
    rules = {}
    with open("input") as f:
        for line in f:
            line_regex = re.compile("^(.+)\s=>\s(.+)$")
            c = line_regex.match(line)            
            rules[c.group(1)] = "".join(c.group(2))
   
    return rules

def break_squares(pattern):
    size = 2 if (pattern.index('/') % 2 == 0) else 3
    pattern = pattern.split("/")
    i = 0
    squares = []
    
    while i < len(pattern):
        rows = []
        r = 0
        while (r < size):
            rows.append(pattern[i + r])
            r += 1
        
        c = 0
        r = 0
        while (c < len(pattern)):
            square = []    
            while r < size:
               col = rows[r][c:c+size]
               square.append(col)     
               r += 1  
            c += size
            r = 0
            squares.append(square) 
        i += size

    return squares

def expand_square(rules, pattern):
    squares = break_squares(pattern)
    
    size = 2 if (pattern.index('/') % 2 == 0) else 3
    num_squares = pattern.index('/') / size
    
    expansions = []
    for s in squares:
        p = "/".join(s)
        expansions.append(find_rule(rules, p).split("/"))        

    rows = 0
    count = 0
    new_pattern = []
    while rows < num_squares:
        squares_to_join = []
        cols = 0
        while cols < num_squares:
            squares_to_join.append(expansions[count])
            count += 1
            cols += 1
        
        for i in range(len(squares_to_join[0])):
            line = []
            for s in squares_to_join:
                line.append(s[i])
            new_pattern.append(line)
        rows += 1
    
    pattern = hash(new_pattern)
    return pattern
    
def expand_iter(rules, pattern, iteration):
    for i in range(iteration):
        pattern = expand_square(rules, pattern)  
          
    return pattern
    
rules = read()
print(expand_iter(rules, ".#./..#/###", 18).count("#"))