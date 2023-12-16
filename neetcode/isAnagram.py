# neetcode problem 2

leetcode_sol_link = 'https://leetcode.com/problems/valid-anagram/submissions/1121069796'

# hashmap approach
# Time Complexity  = O(S+T)
# Space Complexity = O(S+T)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if length is same otherwise it is impossible to 
        # make a anagram

        if len(s) != len(t):
            return False
        
        # make hashmaps to maintain the count of the two strings
        # characters occurences

        hashMap1 , hashMap2 = {}, {}

        for i in range(len(s)):
            hashMap1[s[i]] = 1 + hashMap1.get(s[i],0)
            hashMap2[t[i]] = 1 + hashMap2.get(t[i],0)

        for j in hashMap1:
            if hashMap1[j] != hashMap2.get(j,0):
                return False
        
        return True

# python only approach 
# Counter is python function that does above thing for me 
# its faster and takes less space lol xd
# will not work in interview prob
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

  
