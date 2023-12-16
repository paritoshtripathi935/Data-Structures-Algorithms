# neetcode question 1 

leetcode_sol_link = 'https://leetcode.com/problems/contains-duplicate/submissions/1121024938'

# better solution for better space complexity
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # first we should sort the array 
        # then check the array seq if any number repeats
        # this approach is better for space but not for time

        nums.sort()

        check_number = None

        for n in nums:
            if n == check_number:
                return True
            else:
                check_number = n

        return False

# 1. Implemented above result with sorting the list, which makes it easier to check seq for duplicates.
# 2. The time complexity of the code is O(n log n) since we are looping through the list to check and sorting.
# 3. The space complexity of the code O(1) since we are only storing single variable.


# better solution for better time complexity

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # in this case we are using set for checking the duplicate 
        # since we are sorting the list here better time comeplexity
        # little worse space complexity since we are now storing the values.
      
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
      
# 1. Implemented above result with sorting the list, which makes it easier to check seq for duplicates.
# 2. The time complexity of the code is O(n) since we are looping through the list to check.
# 3. The space complexity of the code O(n) since we are only storing single variable.
