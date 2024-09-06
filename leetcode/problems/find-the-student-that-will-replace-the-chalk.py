# find the students that will reoplace the chalk
# Input -
#   N - Number of students [ 0 to n-1 ]
#   Chalk - Array
#   K - integer [ Number of chalks pieces available  ]
#
# Usage -
#   Whenever a student is solving problems he will use chalk[i] pieces
# to solve the problem. but if number of chalks available present is less than
# required then the student number i to repalced the chalk
#
# output -
#   return the index of student that will reaplce chalk
#
# Approach -
#   Variable for updating the K value
#   A condition to keep checking when chlak is finshed while tracking
# the index of the student
#
# Edge Cases -
#   1. What will happen if there are too much chalks available.
#   2. the normal checks will fail constanly while stuck in checking
# that will execed the alloted time to run this.

from typing import List
class Solution:
    def chalkReplacer_brutefoce(self, chalk: List[int], k: int) -> int:
        current_chalk_count = k

        while True:
            for student in range(0, len(chalk)):
                if current_chalk_count < chalk[student]:
                    return student
                current_chalk_count -= chalk[student]
                print(f'student number {student} uses {chalk[student]} so k = {current_chalk_count}')

    def chalkReplacer_modulo(self, chalk: List[int], k: int) -> int:
        total_chalks_required_for_1_round = sum(chalk)
        k = k % total_chalks_required_for_1_round # this will give us the number of chalks left in last cycle which can't be completed.

        current_chalk_count = k
        for student in range(0, len(chalk)):
            if current_chalk_count < chalk[student]:
                return student
            current_chalk_count -= chalk[student]
            print(f'student number {student} uses {chalk[student]} so k = {current_chalk_count}')

        return -1 # if nothing found return 0

sol = Solution()
chalk = [1,2,3,5]
k = 1000000000
print(sol.chalkReplacer_modulo(chalk=chalk, k=k))


leetcode_sol = 'https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/submissions/1380834637'
