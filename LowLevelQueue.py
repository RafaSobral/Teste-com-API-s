from __future__ import annotations
from typing import Any

EMPTY_NODE_VALUE = '_EMPTY_NODE_VALUE_'

class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f'{self.value}'

    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)

class Queue:
    def __init__(self) -> None:
        self.first: Node | None = None
        self.last: Node | None = None
        self._count = 0

    def push(self, node_value: Any) -> None:
        new_node = Node(node_value)
        if not self.first:  
            self.first = new_node
        else:
            self.last.next = new_node  
        self.last = new_node
        self._count += 1

    def pop(self) -> Node:
        if not self.first:  
            raise EmptyQueueError('The queue is empty.')
        popped_node = self.first
        self.first = self.first.next  
        if not self.first:  
            self.last = None
        self._count -= 1
        return popped_node

    def peek(self) -> Node | None:
        return self.first

    def __len__(self) -> int:
        return self._count

    def __bool__(self) -> bool:
        return bool(self._count)

    def __repr__(self) -> str:
        nodes = []
        current = self.first
        while current:
            nodes.append(repr(current))
            current = current.next
        return f'Queue([{", ".join(nodes)}])'

if __name__ == "__main__":
    queue = Queue()
    queue.push('A')
    print(queue)
    queue.push('B')
    print(queue)
    queue.push('C')
    print(queue)
    print(queue.pop())
    print(queue)
