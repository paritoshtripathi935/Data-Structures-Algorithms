
leetcode_sol_link  = f'https://leetcode.com/problems/group-anagrams/submissions/1122760545'

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dict
        hash_table = defaultdict(list)

        # sort the string we dont need to maintain so many keys 
        for word in strs:
            sorted_word = ''.join(sorted(word))
            hash_table[sorted_word].append(word)

        # Extract values from the defaultdict 
        anagram_groups = list(hash_table.values())

        return anagram_groups

# 1. Implemented a solution to group anagrams by sorting each word in the list. Sorting the words makes it easier to identify anagrams by ensuring that anagrams have the same sorted representation.
# 2. The time complexity of the code is O(n log n) since we iterate through the list, sorting each word which takes O(m log m) time for each word, where 'n' is the number of words and 'm' is the average length of the words.
# 3. The space complexity of the code is O(1) since we only use a constant amount of additional space for variables. The actual grouping is done in-place within the existing list structures, avoiding significant additional memory usage.
