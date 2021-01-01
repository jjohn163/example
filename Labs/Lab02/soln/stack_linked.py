
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class Stack:
    def __init__(self, capacity):
        self.capacity= capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return self.num_items == self.capacity

    def push(self, item):
        if self.num_items == self.capacity:
            raise IndexError
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.num_items += 1

    def pop(self):
        if self.is_empty():
            raise IndexError
        temp = self.head.data
        self.head = self.head.next
        self.num_items -= 1
        return temp

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.head.data 

    def size(self):
        return self.num_items
