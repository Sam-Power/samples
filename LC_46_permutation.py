class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for sayi in nums:
            result = [ i + [j] for i in result for j in nums if j not in i  ]
        return result

"""
46. Permutations
Medium

4637

114

Add to List

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""