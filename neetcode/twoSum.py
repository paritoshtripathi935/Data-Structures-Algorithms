# neetcode problem 3

leetcode_sol_link = 'https://leetcode.com/problems/two-sum/submissions/897179925'

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums): # enumerate returns index and value of list
            if target - num in seen: # if target - num is in seen dictionary then
                return [seen[target - num], i]
            seen[num] = i
