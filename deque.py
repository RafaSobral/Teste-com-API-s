class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None 

class Deck:
    def __init__(self):
        self.left = None 
        self.tight = None 
        self._size = 0 

def push_left(self,elem):
    node = Node(elem)
    if self.left is None:
        self.left = node
        self.right = node 
    else:
        self.left.previous = node 
        node.next = self.left
        self.left = node 
    self._size +=1

def push_right(self,elem):
    node = Node(elem)

    if self.right is None:
        self.right = node 
        self.left = node 
    else:
        node.previous = self.right
        self.right.next = node 
        self.right = node 
    self._size += 1

def pop_left(self):
    if self.empty():
        return 'Deque Vazio'
    elem = self.left.data
    self.left = self.left.next 
    self.left.previous = None
    self._size -= 1
    return elem 

def peek_left(self):
    if self.empty():
        return 'Deque Vazio'
    return self.left.data
    
def pop_right(self):
    if self.empty():
        return 'Deque Vazio'
    elem = self.right.data
    self.right = self.right.previous 
    self.right.next = None
    self._size -= 1
    return elem 

def peek_right(self):
    if self.empty():
        return 'Deque Vazio'
    return self.right.data

def __len__(self):
    return self._size

def empty(self):
    return len(self) == 0

def __repr__(self):
    if self.empty():
        return 'Deque Vazio'
    
    p = self.left
    s = 'left <<'
    while(p):
        s += str(p.data)
        p = p.ext
        if p:
            s += ' | '

    s += ' >> right'
    return s