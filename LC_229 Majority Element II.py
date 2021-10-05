"""Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # nums = [3,2,3]
        l = len(nums)
        if l < 3 :
            return list(set(nums))
        else:
            #print(l/3)
            #print(nums.count(3))
            return [i for i in set(nums) if nums.count(i) > l/3]


# Runtime: 108 ms, faster than 95.43% of Python3 online submissions for Majority Element II.
# Memory Usage: 15.6 MB, less than 30.13% of Python3 online submissions for Majority Element II.