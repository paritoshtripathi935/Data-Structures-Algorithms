class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique elements
        seen = set()
        
        # Iterate through each element in the nums array
        for num in nums:
            # If the current element is already in the set, it's a duplicate
            if num in seen:
                return True
            # Otherwise, add the current element to the set
            seen.add(num)
        
        # If no duplicates were found, return False
        return False
    
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""