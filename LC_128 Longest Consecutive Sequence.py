"""
128. Longest Consecutive Sequence
Hard

4113

203

Add to List

Share
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution:
    def longestConsecutive(self, nums)  :
        max = temp = 0
        if nums == []:
            return 0
        else:
            c = sorted(nums)
            for i in range(len(nums)):
                if i+1 < len(nums):
                    if c[i+1] - c[i] == 1:
                        temp += 1
                    elif c[i+1] - c[i] == 0:
                        pass
                    else:
                        temp = 0
                if temp > max:
                    max = temp
            return max+1
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))