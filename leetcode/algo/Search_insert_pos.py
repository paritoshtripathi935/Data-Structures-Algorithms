class Solution:
    def searchInsert(self, nums,target):
        low , high = 0 , len(nums)-1
        while low <= high:
            mid = low + (high-low) // 2  # if high is greater than low
            if nums[mid] == target:
                return mid
            if nums[mid] > target:  # if target is smaller ignore right half
                high = mid - 1
            else:
                low = mid + 1
            
        return low
