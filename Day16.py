get_command = {
  's': lambda p, command: spin(p, command),
  'x': lambda p, command: exchange(p, command),
  'p': lambda p, command: partner(p, command)
}

def spin(p, command):
    #print("spin", p, command)
    n = int(command[0:])
    prefix = p[-n:]
    return prefix + p[0:-n]

def exchange(p, command):
    #print("exchange", p, command)
    a = int(command[0:command.index('/')])
    b = int(command[command.index('/') + 1:])
    #print("a=", a, " b= ", b)
    t = p[b]
    p[b] = p[a]
    p[a] = t  
    return p

def partner(p, command):
    #print("partner", p, command)
    a = command[0:command.index('/')]
    b = command[command.index('/') + 1:]
    
    return exchange(p, str(p.index(a)) + '/' + str(p.index(b)))

def read():
    with open('input') as f:
        return f.readline()

def process(input):
    programs = ['b', 'k', 'g', 'c', 'd', 'e', 'f', 'i', 'h', 'o', 'l', 'n', 'p', 'm', 'j', 'a']
    commands = input.split(',')
    memory = {}
    i = 999999961 # cycle of 60 calculated beforehand
    init_key = ''.join(programs)
    key = ''
    while i < 1000000000:
        key = ''.join(programs)
        if key not in memory:
            for c in commands:
                programs = get_command[c[0]](programs, c[1:])

            memory[key] = programs[:]
        else:            
            programs = memory[key][:]                   

        i += 1

    print (''.join(programs))

process(read())
