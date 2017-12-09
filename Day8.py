import re
import operator

reg = {}

if_statement = {
  '<': lambda x,y: reg[x] < y,
  '>': lambda x,y: reg[x] > y,
  '<=': lambda x,y: reg[x] <= y,
  '>=': lambda x,y: reg[x] >= y,
  '!=': lambda x,y: reg[x] != y,
  '==': lambda x,y: reg[x] == y
}

def read():        
    node_r = re.compile('^([a-z]+)\s([a-z]+)\s(-?[0-9]+)\s(?:if)\s([a-z]+)\s([<|>|=|!]+)\s(-?[0-9]+)$')    
    max_val = 0
    with open('input') as f:
        for line in f:
            m = node_r.match(line)
            if (m != None):
                reg1 = m.group(1)
                op1 = m.group(2)
                val1 = int(m.group(3))

                reg2 = m.group(4)
                op2 = m.group(5)
                val2 = int(m.group(6))

                if (reg1 not in reg):
                    reg[reg1] = 0
                if (reg2 not in reg):
                    reg[reg2] = 0

                
                if (if_statement[op2](reg2, val2)):
                    if (op1 == 'inc'):
                        reg[reg1] += val1
                    else:
                        reg[reg1] -= val1
                    
                    if (reg[reg1] > max_val):
                        max_val = reg[reg1]
    print(max_val)

read()
print(reg[max(reg, key=reg.get)])

