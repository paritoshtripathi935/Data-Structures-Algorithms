# given
#   - nums
#   The concatenation of two numbers is the number formed by concatenating their numerals.
# First Aproch
# While:
    # break if nums is empty
# keep adding the 0 index element and -1 element in temp_conactcation_value
# remove the last and first element and append temp_conactcation_value in concatenation_value
# handle case where 1 element is left int the end
# and return concatenation_value
#
# Second Approach -
# maintain a pointer left and right since using pop and remove operation take too much time
#



from typing import List
class Solution:
    def findTheArrayConcVal__first_approach(self, nums: List[int]) -> int:
        concatenation_value = 0

        while True:
            if len(nums) <= 0:
                return concatenation_value

            if len(nums) >= 2:
                temp_value = f'{nums[0]}{nums[-1]}'
                nums.remove(nums[0])
                nums.pop()
                concatenation_value += int(temp_value)

            else:
                concatenation_value += nums[0]
                nums.remove(nums[0])

        return concatenation_value

    def findTheArrayConcVal__optmized_approach(self, nums: List[int]) -> int:
        concatenation_value = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            if left == right:
                concatenation_value += nums[left]
            else:
                temp_value = f'{nums[left]}{nums[right]}'
                concatenation_value += int(temp_value)

            left += 1
            right -= 1

        return concatenation_value
sol = Solution()
nums = [72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10,33,72,97,60,79,68,25,63,82,88,60,37,60,44,14,62]
print(sol.findTheArrayConcVal__first_approach(nums=nums))
nums = [72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10,33,72,97,60,79,68,25,63,82,88,60,37,60,44,14,62]
print(sol.findTheArrayConcVal__optmized_approach(nums=nums))


leetcode_url = 'https://leetcode.com/problems/find-the-array-concatenation-value/submissions/1381139006'
