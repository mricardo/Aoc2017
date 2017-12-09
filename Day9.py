def groups(s):
    stack = list()    
    garbage = list()
    i = 0
    groups = 0
    non_cancelled = 0
    previous_erase = False    
    while i < len(s):
        symbol = s[i]
        if symbol == "<" and not previous_erase and not garbage:      
            garbage.append("<")
        elif symbol == ">" and not previous_erase:                
            if (garbage):
                garbage.pop()
        elif symbol == "{" and not previous_erase:
            if not garbage:
                stack.append(symbol)
            else:
                non_cancelled += 1
        elif symbol == "}" and not previous_erase:
            if stack and not garbage:            
                groups += len(stack)
                stack.pop()       
            elif garbage:
                non_cancelled += 1         
        elif symbol == "!" and not previous_erase:
            previous_erase = True
        else: 
            if not previous_erase and garbage:         
                non_cancelled += 1
            previous_erase = False

        i += 1
    
    #print ("Total groups=",groups)
    print ("Non cancelled=",non_cancelled)    

def read():     
     with open('input') as f:
        for line in f:
          groups(line.strip(' \t\n\r'))    

read()
