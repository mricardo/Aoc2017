import sys
import re

sent = [0, 0]

def idx(X):    
    return ord(X.strip()) - ord('a')

def value(regs, Y):
    if isinstance(Y, int):
        return Y

    if Y.strip().isdigit() or (Y.strip().startswith('-') and Y.strip()[1:].isdigit()):
        return int(Y.strip())

    return regs[idx(Y)]

def snd(p, ip, regs, messages, X): 
    global sent
    sent[p]+=1
    messages.append(value(regs, X))
    return ip + 1

def rcv(ip, messages, regs, X): 
    if not messages:
        return (messages, True, ip)
    
    regs[idx(X)] = value(regs, messages[0])
    return (messages, False, ip + 1)

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
    
def jgz(ip, regs, X, Y):    
    if value(regs, X) > 0:    
        return ip + value(regs, Y)        
    return ip + 1

def read_instrs():    
    with open("input") as f:
        instrs = f.readlines()
    
    return instrs

#7747
#7620
def run(p, ip, messages_0, messages_1, regs, instrs):
    regs[idx('p')] = p    

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
            ip = snd(p, ip, regs, messages_1, c.group(2))

        if (c.group(1) == 'rcv'):
            (messages_0, blocked, ip) = rcv(ip, messages_0, regs, c.group(2))
            if (blocked):
                return (ip, blocked, messages_0, messages_1)
            else:
                messages_0 = messages_0[1:]

        if (c.group(1) == 'jgz'):            
            ip = jgz(ip, regs, c.group(2), c.group(3))
    
    return (-1, False, messages_0, messages_1)


def run_both():
    global sent
    messages1 = []
    messages0 = []
    ip0 = 0
    ip1 = 0
    blocked0 = False
    blocked1 = False
    regs0 = [0 for x in range(16)]    
    regs1 = [0 for x in range(16)]    
    instrs = read_instrs()
   
    while True:        
        (ip0, blocked0, messages0, messages1) = run(0, ip0, messages0, messages1, regs0, instrs)
        (ip1, blocked1, messages1, messages0) = run(1, ip1, messages1, messages0, regs1, instrs)
        if (blocked0 and blocked1 and not messages0 and not messages1):
            break

    print("Sent by 0: ", sent[0])    
    print("Sent by 1: ", sent[1])

run_both()