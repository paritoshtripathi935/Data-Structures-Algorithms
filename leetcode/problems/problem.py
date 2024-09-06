# given
#   - 2d Arrays aka Matrix
#   - score = 0
#
# Removed largest element from each row from the matrix
# add this number to score
# in case of ties remove anyone
# return final score
#
# brute force Approch
#   - MainTain a While Loop
#   - add a condition a check if matrix is empty or not in each iteration. [ becasue we not to keep processing until matrix is until. ]
#   - Loop through each list of matrix and extract max number in list removed numbers then remove that number from list until list is empty.
#   - keep appending score after each layer interation of the matrix.
#   - Thus, the overall complexity is O(m * n²), where n is the number of rows and m is the number of columns in nums.

# Optmized Apprroch
#   - Sort the nums before hand so you use pop instead that has lower time complexity.
#   - Thus, the overall complexity is O(n * m log m), which is much faster than the brute-force version.

from typing import List
import time
class Solution:
    def is_matrix_empty(self, matrix):
      return not matrix or all(not row for row in matrix)

    def matrixSum_bruteforce(self, nums: List[List[int]]) -> int:
        start = time.time()
        score = 0
        while True:
            removed_numbers = []

            if self.is_matrix_empty(nums):
                break

            for layer1 in nums:
                if len(layer1) <= 0:
                    continue

                removed_numbers.append(max(layer1))
                layer1.remove(max(layer1))

            score += max(removed_numbers)

        end = time.time()
        total_time_seconds = end - start  # Time in seconds

        print(f"Time taken: {total_time_seconds:.6f} seconds")  # Pr
        return score

    def matrixSum_optimized(self, nums: List[List[int]]) -> int:
        start = time.time()
        score = 0

        # Sort each row in descending order so max is always at the end
        for i in range(len(nums)):
            nums[i].sort(reverse=True)

        while True:
            removed_numbers = []

            if self.is_matrix_empty(nums):
                break

            for layer1 in nums:
                if len(layer1) <= 0:
                    continue

                removed_numbers.append(layer1.pop())

            score += max(removed_numbers)

        end = time.time()
        total_time_seconds = end - start

        print(f"Time taken: {total_time_seconds:.6f} seconds")
        return score

sol = Solution()
nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
print(sol.matrixSum_bruteforce(nums=nums))
nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
print(sol.matrixSum_optimized(nums=nums))
