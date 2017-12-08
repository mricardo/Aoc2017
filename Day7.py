import re
nodes = list()        

class Node:
    def __init__(self, name, weight = None, parent = None):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = list()           

    def add_child(self, child):
        self.children.append(child)

    def last_root(self):
        return (self.children and not self.children[0].children)

def search(name):
    for n in nodes:
        if (n.name == name):
            return n
    return None

def insert(name, weight = None, parent = None):   
    node = search(name)

    if (node == None):
        node = Node(name, weight, parent)
        nodes.append(node)
    
    if (weight):
        node.weight = int(weight)

    if (parent):
        node.parent = parent
        parent.add_child(node)

    return node

def root():
    for n in nodes:
        if (n.parent == None):
            return n
    return None

def sum_node(node):
    if not node.children:
        return node.weight

    total = 0
    for c in node.children:
        total += sum_node(c)

    return node.weight + total

def weight_balence(root, weight, excess):
    s = [0] * len(root.children)
    for i, c in enumerate(root.children):
        s[i] = sum_node(c)
      
    sorted_s = sorted(s, reverse=True)
   
    diff = sorted_s[0] - sorted_s[1]
    if (diff == 0):
        return weight - excess

    idx = s.index(sorted_s[0])    
    child = root.children[idx]
    return weight_balence(child, child.weight, diff)
  
def read():
    node_r = re.compile('^([a-z]+)\s\(([0-9]+)\)(?:\s->\s)?(([a-z]+(,\s)?)+)?')    

    with open('input') as f:
        for line in f:
            m = node_r.match(line)
            if (m != None):
                name = m.group(1)
                weight = m.group(2)
                children = m.group(3)
                              
                parent = insert(name, weight)
                if (children != None):
                    children = [c.strip() for c in children.split(',')]
                    for c in children:
                        insert(c, parent=parent)

read()
root = root()
print(root.name)
print(weight_balence(root, root.weight, 0))
