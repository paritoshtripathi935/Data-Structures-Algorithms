# 2D array called nums
#
# return largest prime that lies on the diagonals of nums
# if none found return 0
#
# extra - An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
# if a number is on diagonals
# condition 1 = nums[i][i] = val
# condition 2 = nums[i][nums.length - i - 1] = val

# approach
# store all the value of diagonal and then find largest prime in the arrys

from typing import List

class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        diagonals = []
        n = len(nums)
        k = n - 1

        for i in range(len(nums)):
            diagonals.append(nums[i][i])
            diagonals.append(nums[i][k])
            k-=1

        diagonals.sort(reverse=True)
        for i in diagonals:
            if self.is_prime(i):
                return i
        return 0



sol = Solution()
nums = [[1,2,3],[5,6,7],[9,10,11]]
print(sol.diagonalPrime(nums=nums))
