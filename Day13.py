import re
layer = [(0,0,0)] * 93

def tick_clock(l):
    for i, (s, r, d) in enumerate(l):
        if r:
            if d:
                if s + 1 < r:
                    l[i] = (s+1, r, d)
                else:
                    l[i] = (s-1, r, 0)
            elif not d:
                if s - 1 >= 0:
                    l[i] = (s-1, r, d)
                else:
                    l[i] = (1, r, 1)
    return l

def simulate(l):
    severity = 0
    for i in range(len(l)):
        (s, r, d) = l[i]        
        if (s == 0 and r > 0):
            severity += i * r
        
        tick_clock(l)        

    print ("severity: ", severity)   

def simulate_min(l):
    ticks = 0
    maxx = -1
    while True:
        try_l = l[:]
        caught = False
        for i in range(len(try_l)):            
            (s, r, d) = try_l[i]        
            if (s == 0 and r > 0):
               caught = True
               break
            
            tick_clock(try_l)
        
        if not caught:
            print("ticks:", ticks)
            break        

        tick_clock(l)                
        ticks += 1

def read():
    pattern = re.compile('^(.+):\s(.+)$')    
   
    with open('input') as f:        
        for line in f:
            m = pattern.match(line)
            layer[int(m.group(1))] = (0, int(m.group(2)), 1)
            

read()      
#simulate(layer[:])
simulate_min(layer[:])