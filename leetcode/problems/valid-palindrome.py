class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s) - 1         

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not self.alphnum(s[left_pointer]):
                left_pointer += 1

            while right_pointer > left_pointer and not self.alphnum(s[right_pointer]):
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            
            left_pointer, right_pointer = left_pointer + 1, right_pointer - 1

        return True

    def alphnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))