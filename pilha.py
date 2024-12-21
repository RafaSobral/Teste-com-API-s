class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack: 
    def __init__(self):
        self.top = None 
        self.size = 0 

def push(self,elem):
    node = Node(elem)
    node.next = self.top
    self.top = node 
    self.size += 1 

def pop(self):
    if self.empty():
        return 'Pilha Vazia'
    node = self.top 
    self.top = self.top.next
    self._size -=1
    return node.data 

def peek(self):
    if self.empty():
        return 'Pilha Vazia'
    return self.top.data


def __len__(self):
    return self._size

def empty(self):
    return len(self) == 0

def __repr__(self):
    if len(self) == 0:
        return 'Pilha Vazia'

    s = ''
    p = self.top
    while(p):
        s += str(p.data) + '\n'
        p = p.next
    return s