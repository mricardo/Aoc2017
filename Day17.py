def spinlock(steps, max_insertions):
    current_position = 0
    buffer = [0]

    i = 0
    
    steps_taken = 0
    current_position = 0
    value = 1
    before = None
    while (i < max_insertions):
        j = 0
        while (j < steps):
            current_position = (current_position + 1) % len(buffer)
            j += 1
                       
        if (len(buffer) == 1):
            current_position = 1
            buffer.append(value)
        else:
            buffer = buffer[0:current_position + 1] + [value] + buffer[current_position + 1:]   
            current_position += 1     
    
        if (not before or before != buffer[buffer.index(0) + 1]):
            before = buffer[buffer.index(0) + 1]
            print("i=", i, "=>", before)
        value += 1
        i += 1
    
    return buffer[buffer.index(0) + 1]   

def spinlock_0(steps, max_insertions):
    current_position = 0
  
    value = 1
    size = 0
    value_0 = -1
    while (size < max_insertions):
        j = 0
        
        while (j < steps):
            current_position = (current_position + 1) % (size + 1)
            j += 1
        
        
        if (size == 0 or current_position == 0):            
            value_0 = value            
            print("i=", size, "=>", value_0)
        
        current_position += 1
        size += 1
        value += 1
       
    return value_0   

print(spinlock_0(344, 50000000))