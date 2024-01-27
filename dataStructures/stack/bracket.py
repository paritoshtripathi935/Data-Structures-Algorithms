from sys import maxsize 

class Solution:
    def __init__(self):
        self.stack = self.createStack()

    def createStack(self):
        stack = []
        return stack

    def isEmpty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if (self.isEmpty(self.stack)): 
            return str(-maxsize -1)
        
        return self.stack.pop() 
  
    def push(self, item):
        self.stack.append(item) 
  
    def peek(self): 
        if (self.isEmpty(self.stack)): 
            return str(-maxsize -1)
        return self.stack[len(self.stack) - 1] 

    def isValid(self, s: str) -> bool:
        open_brackets = ["(", "{", "["]

        if len(s) <= 1:
            return False
        
        
        for i in s:
            if i in open_brackets:
                self.push(i)

            else:
                
                if self.isEmpty():
                    return False
                
                top = self.peek()
                self.pop()

                if top == '(':
                    if i != ')':
                        return False
                if top == '{':
                    if i != '}':
                        return False
                if top == '[':
                    if i != ']':
                        return False
                    

        if self.isEmpty():
            return True

        return False
    