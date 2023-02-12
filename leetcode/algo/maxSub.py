class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSub to the first element of nums
        maxSub = nums[0]
        # Initialize curSum to 0
        curSum = 0
        
        # Iterate through each element in the nums array
        for n in nums:
            # If the current sum is less than 0, reset it to 0
            if curSum < 0:
                curSum = 0
            # Add the current element to the current sum
            curSum += n
            # Update maxSub to be the maximum of the current maxSub and curSum
            maxSub = max(maxSub, curSum)
        
        # Return the maximum sum found
        return maxSub
