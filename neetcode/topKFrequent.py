
leetcode_sol_link  = 'https://leetcode.com/problems/top-k-frequent-elements/submissions/1124506020'

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        # Sort the numbers based on their frequency in descending order
        sorted_nums = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

        # extract top k elements
        result = [num for num, _ in sorted_nums[:k]]
        
        return result
