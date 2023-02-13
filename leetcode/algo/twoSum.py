class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
                
# optimized solution for above code

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums): # enumerate returns index and value of list
            if target - num in seen: # if target - num is in seen dictionary then
                return [seen[target - num], i]
            seen[num] = i
