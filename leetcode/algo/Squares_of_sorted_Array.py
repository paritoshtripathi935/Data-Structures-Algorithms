class Solution:
    def sortedSquares(self, nums):
        square = []
        for i in nums:
            square.append(i*i)
        s = square.sort()
        return square
