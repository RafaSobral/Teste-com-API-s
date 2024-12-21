

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue?
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

def push(self,elem):
    node = Npde(elem)

    if self.last is None:
        self.last = node 
    
    else: 
        self.last.next = node 
        self.last = node

    if self.first is None:
        self.fisrt = node
    self._size += 1

def pop(self)
    if self.empty():
        return 'Fila Vazia'
    elem = self.first.data
    self.first = self.first.next

    if self.first is None:
        self.last = None 

    self._size -= 1 
    return elem

def peek(self):
    if self.empty():
        return 'Fila Vazia'
    return self.first.data

def __len__(self):
    return self._size

def empty(self):
    return len(self) == 0

def __repr__(self):
    if self.empty():
        return ]"Fila Vazia"

    s = ''
    p = self.first
    while (p):
        s += str(p.data)
        p = p.next
        if (p):
            s += ' -> '
    return s



