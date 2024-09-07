# Topic - DP
# Given -
#   string s of lenght N
#   s[i] is either 'D' or 'I' means Increasing
#
#   Permutation perm of n + 1 integers of all integer in range
#    [0,n] is called a valid permuatation if for all valid i.
#    If s[i] == 'D', then perm[i] > perm[i + 1], and
#    If s[i] == 'I', then perm[i] < perm[i + 1].
# Return the number of valid permutations perm.
# Since the answer may be large, return it modulo 10^9 + 7.

# First approach
#   outpit = 0
#   perm = range(0, len(s))
#   - for i in range(len(s)):
    # if s[i] == 'D':
        # if perm[i] > perm[i+1]:
            # output += 1
#   elif s[i] == 'I':
    # if perm[i] < perm[i+1]:
        # output += 1
    # return output


class Solution:
    def permutations(self, arr):
        # Base case: If the array is empty, return an empty list.
        if len(arr) == 0:
            return []

        # Base case: If the array has one element, return it as the only permutation.
        if len(arr) == 1:
            return [arr]

        # Recursive case
        perms = []
        for i in range(len(arr)):
            # Choose an element to permute with the rest of the array
            current = arr[i]
            remaining = arr[:i] + arr[i+1:]

            # Generate all permutations of the remaining elements
            for p in self.permutations(remaining):
                perms.append([current] + p)

        return perms

    def numPermsDISequence(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        output = 0
        perms = self.permutations(list(range(n+1)))

        for j in range(len(perms)):
            for i in range(n):
                if s[i] == "D":
                    if perms[j][i] > perms[j][i + 1]:
                        output += 1

                elif s[i] == "I":
                    if perms[j][i] < perms[j][i + 1]:
                        print(perms[j])
                        output += 1

        return output


sol = Solution()
s = "DID"
print(sol.numPermsDISequence(s=s))

# Leetcode HARD need to understand DP
