"""78. Subsets
Medium

5712

111

Add to List

Share
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rep = []
        for i in range(len(nums)+1):
            rep.extend(list(itertools.combinations(nums,i)))
        return rep

"""Success
Details 
Runtime: 32 ms, faster than 77.22% of Python3 online submissions for Subsets.
Memory Usage: 14.4 MB, less than 51.86% of Python3 online submissions for Subsets.
"""