# Given -
#   1 - Indexed array of Integers = Numbers [Sorted Aseceding]
#   2 - an element k called target
# Return -
#   1. Indexes of element such that sum of any elements in array is equal to
#   target number

# Constraints -
#   Your solution must use only constant extra space.

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1

        while lp < rp:
            curr_sum = numbers[lp] + numbers[rp]
            if curr_sum > target:
                rp -= 1
            elif curr_sum < target:
                lp += 1
            else:
                return [lp + 1, rp + 1]
        return 0

sol = Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([2,3,4],6))
print(sol.twoSum([-1,0],-1))
print(sol.twoSum([3,24,50,79,88,150,345],200))
