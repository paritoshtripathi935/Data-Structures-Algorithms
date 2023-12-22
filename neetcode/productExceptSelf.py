leetcode_sol_link = f'https://leetcode.com/problems/product-of-array-except-self/submissions/1125671886'

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = 1
        suffix[n-1] = 1

        output = []

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(0,n):
            output.append(prefix[i] * suffix[i])
        
        return output

# Time Complexity O(n)
# Space Complexity O(n)
