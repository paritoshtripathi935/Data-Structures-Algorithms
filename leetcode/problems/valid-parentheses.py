#First-In/Last-Out (FILO) manner
# Input -
#   String S
#

class Solution:
    def isValid(self, s: str) -> bool:
        string_stack = []
        opening_characters = ["(", "{", "["]

        if len(s) <= 1:
            return False

        for i in s:
            if i in opening_characters:
                string_stack.append(i)
            else:
                top = string_stack[-1]
                string_stack.pop()

                if top == '(':
                    if i != ')':
                        return False
                if top == '{':
                    if i != '}':
                        return False
                if top == '[':
                    if i != ']':
                        return False

        if len(string_stack) == 0:
            return True

        return False


sol = Solution()
print(sol.isValid("([])"))
