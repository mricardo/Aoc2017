import sys
import re

mul_exec = 0

def idx(X):      
    return ord(X.strip()) - ord('a')

def value(regs, Y):
    if Y.strip().isdigit() or (Y.strip().startswith('-') and Y.strip()[1:].isdigit()):
        return int(Y.strip())
    return regs[idx(Y)]
    
def sett(ip, regs, X, Y):
    regs[idx(X)] = value(regs, Y)
    return ip + 1

def sub(ip, regs, X, Y):
    regs[idx(X)] -= value(regs, Y)   
    return ip + 1 

def mul(ip, regs, X, Y):
    global mul_exec
    regs[idx(X)] *= value(regs, Y)
    mul_exec += 1
    return ip + 1

def jnz(ip, regs, X, Y):    
    if value(regs, X) != 0:    
        return ip + value(regs, Y)       
    return ip + 1

def jgz(ip, regs, X, Y):
    if value(regs, X) > 0:    
        return ip + value(regs, Y)        
    return ip + 1

def read_instrs():    
    with open("input") as f:
        instrs = f.readlines()
    
    return instrs

def run():
    regs = [0 for x in range(8)]
    ip = 0
    instrs = read_instrs()
    regs[0] = 0 
    while ip < len(instrs):           
        instr = instrs[ip]
        print("ip: ", ip, instr)
        line_regex = re.compile("^([a-z]+)\s([a-z0-9]+)(\s.+)?")
        c = line_regex.match(instr)
        
        if (c.group(1) == 'set'):
            ip = sett(ip, regs, c.group(2).strip(), c.group(3).strip())
        
        if (c.group(1) == 'sub'):
            ip = sub(ip, regs, c.group(2).strip(), c.group(3).strip())

        if (c.group(1) == 'mul'):    
            ip = mul(ip, regs, c.group(2).strip(), c.group(3).strip())
        
        if (c.group(1) == 'jnz'):
            ip = jnz(ip, regs, c.group(2).strip(), c.group(3).strip())
        
        if (c.group(1) == 'jgz'):
            ip = jgz(ip, regs, c.group(2).strip(), c.group(3).strip())
     
        print(regs)

run()
print(mul_exec)
