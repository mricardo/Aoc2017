def init_memory():    
   with open('input', 'r') as f:
       line = f.readline()
   
   return [int(n) for n in line.split('\t')]     

def digest(m):
    return ''.join(str(x) for x in m)
    

def count_cycles(memory):
    cycles = 0
    banks = len(memory)
    configurations = dict()

    while((digest(memory) in configurations) == False):        
        configurations[digest(memory)] = 1
        cycles += 1
      
        m = max(memory)
        distribution = 1
        
        idx = memory.index(m)
        memory[idx] = 0
        
        idx += 1
        while (m > 0):
            if (distribution > m):
                distribution = m
                
            memory[idx % banks] += distribution
            m -= distribution        
            idx += 1
            
    return [cycles, memory]   

def duplicated_state(memory):
    res = count_cycles(memory)
    res = count_cycles(res[1])
    return res[0]
               
print(count_cycles(init_memory())[0])
print(duplicated_state(init_memory()))