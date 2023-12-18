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
