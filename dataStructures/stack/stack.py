# Code for making a stack structure

# first explain what is stack 
# It is linear data structure that follows a particular order
# in which the operations are performed. the order may be LIFO (Last in First Out)
# or FILO (First in Last out).

# LIFO implies the element that is inserted last comes out first
# FILO implies that the element is inserted first, comes out last.

# To implement a stack, it is required to maintain the pointer to the top of stack 
# which is the last element to be inserted because we can access the elements
# only on the top of the stack.

# Basic Operations on Stack
# push() to insert an element into the stack.
# pop() to remove an element from the stack.
# top() Returns the top element of the stack.
# isEmpty() returns true if stack is empty else false.
# size() return size of stack.

# Time Complexity
# Operations Complexity
# push()   O(1)
# pop()    O(1)
# isEmpty  O(1)
# size()   O(1)

from sys import maxsize 

class Stack:
    def __init__(self):
        pass
    
    def createStack(self):
        stack = []
        return stack

    def isEmpty(self, stack):
        return len(stack) == 0
    
    def pop(self, stack):
        if (self.isEmpty(stack)): 
            return str(-maxsize -1)
        
        return stack.pop() 
  
    def push(self, stack, item):
        stack.append(item) 
        print(item + " pushed to stack ")
  
    def peek(self, stack): 
        if (self.isEmpty(stack)): 
            return str(-maxsize -1)
        return stack[len(stack) - 1] 





