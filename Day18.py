import sys
import re

last_played_sound = None

def idx(X):    
    return ord(X.strip()) - ord('a')

def value(regs, Y):
    if Y.strip().isdigit() or (Y.strip().startswith('-') and Y.strip()[1:].isdigit()):
        return int(Y.strip())
    return regs[idx(Y)]

def snd(ip, regs, X): 
    global last_played_sound
    last_played_sound = regs[idx(X)]    
    return ip + 1
    
def sett(ip, regs, X, Y):
    regs[idx(X)] = value(regs, Y)
    return ip + 1

def add(ip, regs, X, Y):
    regs[idx(X)] += value(regs, Y)   
    return ip + 1 

def mul(ip, regs, X, Y):
    regs[idx(X)] *= value(regs, Y)
    return ip + 1

def mod(ip, regs, X, Y):
    regs[idx(X)] %= value(regs, Y)
    return ip + 1
    
def rcv(ip, regs, X):  
    if regs[idx(X)] > 0 and last_played_sound:
        print(last_played_sound)
        sys.exit()
    return ip + 1

def jgz(ip, regs, X, Y):
    if regs[idx(X)] > 0:    
        return ip + value(regs, Y)        
    return ip + 1

def read_instrs():    
    with open("input") as f:
        instrs = f.readlines()
    
    return instrs

def run():
    regs = [0 for x in range(16)]
    ip = 0
    instrs = read_instrs()

    while ip < len(instrs):           
        instr = instrs[ip]
        line_regex = re.compile("^([a-z]+)\s([a-z0-9]+)(\s.+)?")
        c = line_regex.match(instr)
        if (c.group(1) == 'set'):
            ip = sett(ip, regs, c.group(2), c.group(3))
        
        if (c.group(1) == 'add'):
            ip = add(ip, regs, c.group(2), c.group(3))

        if (c.group(1) == 'mul'):    
            ip = mul(ip, regs, c.group(2), c.group(3))
        
        if (c.group(1) == 'mod'):
            ip = mod(ip, regs, c.group(2), c.group(3))
        
        if (c.group(1) == 'snd'):            
            ip = snd(ip, regs, c.group(2))

        if (c.group(1) == 'rcv'):
            ip = rcv(ip, regs, c.group(2))
        
        if (c.group(1) == 'jgz'):
            ip = jgz(ip, regs, c.group(2), c.group(3))

run()