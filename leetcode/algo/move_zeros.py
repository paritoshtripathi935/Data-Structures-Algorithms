class Solution:
    def moveZeroes(self, nums):
        last= 0
        cur = 0
        for cur in range(0,len(nums)):
            if(nums[cur] != 0):
                nums[last], nums[cur] = nums[cur], nums[last]
                last = last + 1
